# Generated by Django 3.0.3 on 2020-04-01 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20200402_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datamahasiswa',
            name='kelas',
            field=models.CharField(choices=[('IK1A', 'IK1A'), ('IK1B', 'IK1B'), ('IK2A', 'IK2A'), ('IK2B', 'IK2B'), ('IK3A', 'IK3A'), ('IK3B', 'IK3B')], default='IK1A', max_length=4),
        ),
    ]
