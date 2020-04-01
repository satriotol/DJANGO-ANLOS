# Generated by Django 3.0.3 on 2020-04-01 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_userprofileinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataMahasiswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('kelas', models.IntegerField(choices=[(1, 'IK1A'), (2, 'IK1B'), (3, 'IK2A'), (4, 'IK2B'), (5, 'IK3A'), (6, 'IK3B')], default=1)),
            ],
        ),
    ]