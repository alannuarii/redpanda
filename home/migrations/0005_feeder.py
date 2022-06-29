# Generated by Django 3.2.13 on 2022-05-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220517_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(verbose_name='Tanggal')),
                ('jam', models.CharField(max_length=5, verbose_name='Jam')),
                ('kota', models.IntegerField(default=0, verbose_name='Kota')),
                ('tona', models.IntegerField(default=0, verbose_name='Tona')),
                ('kolongan', models.IntegerField(default=0, verbose_name='Kolongan')),
                ('lesabe', models.IntegerField(default=0, verbose_name='Lesabe')),
                ('tamako', models.IntegerField(default=0, verbose_name='Tamako')),
                ('main_line_petta', models.IntegerField(default=0, verbose_name='Main Line Petta')),
                ('petta_kota', models.IntegerField(default=0, verbose_name='Petta Kota')),
                ('main_line_tahuna', models.IntegerField(default=0, verbose_name='Main Line Tahuna')),
                ('kendahe', models.IntegerField(default=0, verbose_name='Kendahe')),
                ('bowongkulu', models.IntegerField(default=0, verbose_name='Bowongkulu')),
                ('kota_tamako', models.IntegerField(default=0, verbose_name='Kota Tamako')),
                ('lapango', models.IntegerField(default=0, verbose_name='Lapango')),
                ('tahuna', models.IntegerField(default=0, verbose_name='Tahuna')),
                ('salurang', models.IntegerField(default=0, verbose_name='Salurang')),
                ('pintareng', models.IntegerField(default=0, verbose_name='Pintareng')),
                ('tahuna_income', models.IntegerField(default=0, verbose_name='Tahuna Income')),
                ('pltd_tahuna', models.IntegerField(verbose_name='PLTD Tahuna')),
                ('pltd_petta', models.IntegerField(verbose_name='PLTD Petta')),
                ('pltd_tamako', models.IntegerField(verbose_name='PLTD Tamako')),
                ('pltd_lesabe', models.IntegerField(verbose_name='PLTD Lesabe')),
                ('total', models.IntegerField(verbose_name='Total')),
            ],
        ),
    ]