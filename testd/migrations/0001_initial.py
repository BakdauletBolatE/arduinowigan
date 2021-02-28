# Generated by Django 3.1.7 on 2021-02-27 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=255, verbose_name='Uid человека')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
        migrations.CreateModel(
            name='StaffSessions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=255, verbose_name='Uid человека')),
                ('check', models.BooleanField(default=0, verbose_name='Чек')),
            ],
            options={
                'verbose_name': 'Сессия',
                'verbose_name_plural': 'Сессий',
            },
        ),
    ]
