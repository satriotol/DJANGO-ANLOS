# Generated by Django 3.0.3 on 2020-06-04 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perusahaan', '0002_auto_20200505_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserKaryawanInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(default='', max_length=256)),
                ('email', models.EmailField(default='', max_length=256)),
                ('alamat', models.TextField(default='')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('nama_perusahaan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='UserKaryawanInfo', to='perusahaan.UserPerusahaanInfo')),
            ],
        ),
    ]