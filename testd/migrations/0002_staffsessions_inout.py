# Generated by Django 3.1.7 on 2021-03-02 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffsessions',
            name='inout',
            field=models.BooleanField(default=0, verbose_name='Вход/Выход'),
        ),
    ]