# Generated by Django 3.0.3 on 2020-06-05 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perusahaan', '0009_auto_20200605_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userkaryawaninfo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
