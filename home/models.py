from array import ArrayType
from pyexpat import model
from django.db import models

# Create your models here.

# Model Unit
class Unit(models.Model):
    nama_unit = models.CharField('Nama Unit', max_length=200)

    def __str__(self):
        return self.nama_unit


# Model Mesin 
class Mesin(models.Model):
    nama_unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name='Nama Unit')
    unit = models.CharField('Unit', max_length=10)
    nama_mesin = models.CharField('Nama Mesin', max_length=200)
    daya_mampu = models.IntegerField('Daya Mampu (kW)')
    is_sewa = models.BooleanField('Sewa')

    def __str__(self):
        return '{} Unit {} ({})'.format(self.nama_unit_id, self.unit, self.nama_mesin)
    

#Model Cost
class Cost(models.Model):
    mesin_id = models.ForeignKey(Mesin, on_delete=models.CASCADE, verbose_name='Nama Mesin')
    fix_cost = models.IntegerField('Total Fix Cost', blank=True, null=True)
    time_base_vcost = models.IntegerField('Total Time Base V-Cost', blank=True, null=True)
    sfc_50 = models.IntegerField('SFC 50% DMN', blank=True, null=True)
    sfc_75 = models.IntegerField('SFC 75% DMN', blank=True, null=True)
    sfc_100 = models.IntegerField('SFC 100% DMN', blank=True, null=True)
    harga_sewa = models.IntegerField('Harga Sewa per kWh (Khusus Sewa)', blank=True, null=True)
    pajak_air = models.IntegerField('Pajak Air Permukaan', blank=True, null=True)
    susut_trafo = models.IntegerField('Susut Trafo', blank=True, null=True)
    susut_jaringan = models.IntegerField('Susut Jaringan (%)', blank=True, null=True)

    def __str__(self):
        return str(self.mesin_id)


# Model Feeder 
class Feeder(models.Model):
    tanggal = models.DateField('Tanggal')
    jam = models.CharField('Jam', max_length=5)
    kota = models.IntegerField('Kota', default=0)
    tona = models.IntegerField('Tona', default=0)
    kolongan = models.IntegerField('Kolongan', default=0)
    lesabe = models.IntegerField('Lesabe', default=0)
    tamako = models.IntegerField('Tamako', default=0)
    main_line_petta = models.IntegerField('Main Line Petta', default=0)
    petta_kota = models.IntegerField('Petta Kota', default=0)
    main_line_tahuna = models.IntegerField('Main Line Tahuna', default=0)
    kendahe = models.IntegerField('Kendahe', default=0)
    bowongkulu = models.IntegerField('Bowongkulu', default=0)
    kota_tamako = models.IntegerField('Kota Tamako', default=0)
    lapango = models.IntegerField('Lapango', default=0)
    tahuna = models.IntegerField('Tahuna', default=0)
    salurang = models.IntegerField('Salurang', default=0)
    pintareng = models.IntegerField('Pintareng', default=0)
    tahuna_income = models.IntegerField('Tahuna Income', default=0)
    pltd_tahuna = models.IntegerField('PLTD Tahuna')
    pltd_petta = models.IntegerField('PLTD Petta')
    pltd_tamako = models.IntegerField('PLTD Tamako')
    pltd_lesabe = models.IntegerField('PLTD Lesabe')
    total = models.IntegerField('Total')

    @property
    def kitTahuna(self):
        totKitTahuna = int(self.kota) + int(self.tona) + int(self.kolongan) + int(self.lesabe) + int(self.tamako) + int(self.main_line_petta)
        return totKitTahuna

    @property
    def kitPetta(self):
        totKitPetta = int(self.petta_kota) + int(self.main_line_tahuna) + int(self.kendahe) + int(self.bowongkulu)
        return totKitPetta

    @property
    def kitTamako(self):
        totKitTamako = int(self.kota_tamako) + int(self.lapango) + int(self.tahuna)
        return totKitTamako

    @property
    def kitLesabe(self):
        totKitLesabe = int(self.salurang) + int(self.pintareng) + int(self.tahuna_income)
        return totKitLesabe

    @property 
    def totalKit(self):
        totKit = int(self.pltd_tahuna) + int(self.pltd_petta) + int(self.pltd_tamako) + int(self.pltd_lesabe)
        return totKit

    def save(self, *args, **kwargs):
        self.pltd_tahuna = self.kitTahuna
        self.pltd_petta = self.kitPetta
        self.pltd_tamako = self.kitTamako
        self.pltd_lesabe = self.kitLesabe
        self.total = self.totalKit
        super(Feeder, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.tanggal)


# Model Har 
class Har(models.Model):
    list_har = (
        ('Standby', 'Standby'),
        ('P1', 'P1'),
        ('P2', 'P2'),
        ('P3', 'P3'),
        ('P4', 'P4'),
        ('P5', 'P5'),
        ('TO', 'TO'),
        ('SO', 'SO'),
        ('MO', 'MO'),
        ('PdM', 'PdM'),
        ('CM', 'CM'),
    )
    mesin_id = models.ForeignKey(Mesin, on_delete=models.CASCADE, verbose_name='Nama Mesin')
    tanggal_jumat =  models.DateField('Tanggal Mulai')
    jumat = models.CharField('Jumat', max_length=20, choices=list_har, default='Standby')
    sabtu = models.CharField('Sabtu', max_length=20, choices=list_har, default='Standby')
    minggu = models.CharField('Minggu', max_length=20, choices=list_har, default='Standby')
    senin = models.CharField('Senin', max_length=20, choices=list_har, default='Standby')
    selasa = models.CharField('Selasa', max_length=20, choices=list_har, default='Standby')
    rabu = models.CharField('Rabu', max_length=20, choices=list_har, default='Standby')
    kamis = models.CharField('Kamis', max_length=20, choices=list_har, default='Standby')
    
def __str__(self):
    return str(self.mesin_id)