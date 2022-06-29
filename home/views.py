from ast import And
from audioop import reverse
from urllib import request
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from .models import Mesin, Unit, Cost, Feeder, Har
from .resource import FeederResource
from .forms import HarForm
from tablib import Dataset
import datetime

# Create your views here.

#Halaman Login
def loginView(request):
    context ={
        'title': 'Login | RedPanda'
    }
    user = None
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'pages/login.html', context)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username dan password Anda tidak tepat')
            return redirect('/login')


#Fitur Logout
class CustomLogoutView(LogoutView):
    template_name = 'pages/login.html'
    next_page = 'login'

    
# Halaman Home 
@login_required(login_url='login')
def home(request):
    engine = Unit.objects.all()
    print(engine)
    context={
        'title': 'Home | RedPanda',
        'active_home': 'active',
        'engines': engine
    }
    return render(request, 'pages/home.html', context)


#https://www.youtube.com/watch?v=Ry4U1OvOq8E
# Halaman Mesin 
@login_required(login_url='login')
def mesin(request, id):
    list_unit = Mesin.objects.filter(nama_unit_id=id)
    nama_unit = list_unit[:1]
    query = request.GET.get('id')
    cost_unit = Cost.objects.filter(mesin_id=query)


    context={
        'title': 'Mesin | RedPanda',
        'list_unit': list_unit,
        'cost':cost_unit,
        'nama_unit': nama_unit
    }
    print(nama_unit)
    return render(request, 'pages/mesin.html', context)


# https://www.youtube.com/watch?v=9i7yg1ltAUw
# Halaman Har
@login_required(login_url='login')
def har(request):
    mesin_kit = Mesin.objects.all()
    query = request.GET.get('tanggal')
    
    if query:
        testime = datetime.datetime.strptime(query, "%Y-%m-%d").date()
    else:
        testime = ''

    if request.method == 'GET':
        data_har = Har.objects.filter(tanggal_jumat=query).order_by('mesin_id').values_list('mesin_id').distinct()
        har_data = []
        for da in data_har:
            tes = Har.objects.filter(mesin_id = da).last()
            har_data.append(tes)

    if request.POST:
        har_form = HarForm(request.POST or None)
        if har_form.is_valid():
            har_form.save()
            url_return = request.POST.get('next')
            return redirect('/har?tanggal='+url_return)

    context={
        'title': 'Pemeliharaan | RedPanda',
        'active_har': 'active',
        'hars': har_data,
        'query':testime,
        'mesins': mesin_kit,
    }
    return render(request, 'pages/har.html', context)




# Halaman Feeder
@login_required(login_url='login')
def feeder(request):
    if request.method == 'GET':
        query = request.GET.get('tanggal')
        data_feeder = Feeder.objects.filter(tanggal=query)
        tanggal = data_feeder[:1]

        beban_feeder = []
        jam = []
        for i in range(len(data_feeder)):
            beban_feeder.append(data_feeder[i].total)
            jam.append(data_feeder[i].jam)

    if request.method == 'POST':
        if request.FILES:
            feeder_resource = FeederResource()
            dataset = Dataset()
            file = request.FILES['feeder']

            if not file.name.endswith('xlsx'):
                messages.warning(request, 'Format file harus .xlsx')
                return redirect('/feeder')

            imported = dataset.load(file.read(), format='xlsx')
            for data in imported:
                value = Feeder(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18])
                value.save()
            messages.success(request, 'File berhasil ditambahkan')
            return redirect('/feeder')

        elif request.POST['tanggal']:
            delete_feeder = Feeder.objects.filter(tanggal=request.POST.get('tanggal')).delete()
            messages.error(request, 'Data berhasil dihapus')
            return redirect('/feeder')

    context={
        'title': 'Feeder | RedPanda',
        'active_feeder': 'active',
        'feeder': data_feeder,
        'tanggal': tanggal,
        'beban': beban_feeder,
        'jam': jam,
    }
    return render(request, 'pages/feeder.html', context)