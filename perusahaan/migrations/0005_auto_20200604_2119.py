# Generated by Django 3.0.3 on 2020-06-04 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perusahaan', '0004_auto_20200604_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userkaryawaninfo',
            name='nama_perusahaan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='perusahaan.UserPerusahaanInfo'),
        ),
    ]