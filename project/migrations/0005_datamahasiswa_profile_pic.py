# Generated by Django 3.0.3 on 2020-04-01 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_datamahasiswa'),
    ]

    operations = [
        migrations.AddField(
            model_name='datamahasiswa',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='foto_mahasiswa'),
        ),
    ]