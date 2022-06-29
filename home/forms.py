from django import forms
from .models import Mesin, Cost, Har

#Form Mesin
class MesinForm(forms.ModelForm):
    class Meta:
        model = Mesin
        fields = [
            'unit',
            'nama_mesin',
            'daya_mampu',
            'is_sewa',
            'nama_unit_id'
        ]


#Form Cost
class CostForm(forms.ModelForm):
    class Meta:
        model = Cost
        fields = [
            'fix_cost',
            'time_base_vcost',
            'sfc_50',
            'sfc_75',
            'sfc_100',
            'harga_sewa',
            'pajak_air',
            'susut_trafo',
            'susut_jaringan',
            'mesin_id',
        ]


# Form Har 
class HarForm(forms.ModelForm):
    class Meta:
        model = Har
        fields = [
            'mesin_id',
            'tanggal_jumat',
            'jumat',
            'sabtu',
            'minggu',
            'senin',
            'selasa',
            'rabu',
            'kamis'
        ]
        widgets = {
            'mesin_id': forms.Select(
                attrs={
    '                   class': 'form-select'
                }
            ),
            'tanggal_jumat': forms.DateInput(
                attrs={
                    'class':'form-control',
                    'type':'date'
                }
            ),
            'jumat' : forms.Select(
                attrs={
                    'class':'form-select'
                }
            ),
            'sabtu' : forms.Select(
                attrs={
                    'class':'form-select'
                }
            ),
            'minggu' : forms.Select(
                attrs={
                    'class':'form-select'
                }
            ),
            'senin' : forms.Select(
                attrs={
                    'class':'form-select'
                }
            ),
            'selasa' : forms.Select(
                attrs={
                    'class':'form-select'
                }
            ),
            'rabu' : forms.Select(
                attrs={
                    'class':'form-select'
                }
            ),
            'kamis' : forms.Select(
                attrs={
                    'class':'form-select'
                }
            ),
        }