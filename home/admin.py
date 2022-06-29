from django.contrib import admin
from .models import Mesin, Unit, Cost, Feeder, Har

# Register your models here.
class MesinAdmin(admin.ModelAdmin):
    list_display = ('nama_unit_id','unit','nama_mesin','daya_mampu','is_sewa',)


class UnitAdmin(admin.ModelAdmin):
    list_display = ('nama_unit',)


class CostAdmin(admin.ModelAdmin):
    list_display = ('mesin_id','fix_cost','time_base_vcost','sfc_50','sfc_75','sfc_100','harga_sewa','pajak_air','susut_trafo','susut_jaringan')


class FeederAdmin(admin.ModelAdmin):
    list_display = ('tanggal','jam','kota','tona','kolongan','lesabe','tamako','main_line_petta','petta_kota','main_line_tahuna','kendahe','bowongkulu','kota_tamako','lapango','tahuna','salurang','pintareng','tahuna_income','pltd_tahuna','pltd_petta','pltd_tamako','pltd_lesabe','total')
    readonly_fields = ('pltd_tahuna','pltd_petta','pltd_tamako','pltd_lesabe','total')


class HarAdmin(admin.ModelAdmin):
    list_display = ('mesin_id','tanggal_jumat','jumat','sabtu','minggu','senin', 'selasa','rabu','kamis')


admin.site.register(Mesin, MesinAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Cost, CostAdmin)
admin.site.register(Feeder, FeederAdmin)
admin.site.register(Har, HarAdmin)
