# Generated by Django 3.0.3 on 2020-04-01 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_datamahasiswa_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datamahasiswa',
            name='kelas',
            field=models.CharField(choices=[('1A', 'IK1A'), ('1B', 'IK1B'), ('2A', 'IK2A'), ('2B', 'IK2B'), ('3A', 'IK3A'), ('3B', 'IK3B')], default='1A', max_length=2),
        ),
    ]
