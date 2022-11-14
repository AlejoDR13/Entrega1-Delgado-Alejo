# Generated by Django 3.2.16 on 2022-11-10 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_auto_20221109_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usarname', models.CharField(max_length=40)),
                ('mail', models.EmailField(max_length=254)),
                ('password', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Suspenso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=40)),
                ('estreno', models.DateField()),
                ('duracion', models.IntegerField()),
                ('epigrafe', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Thriller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=40)),
                ('estreno', models.DateField()),
                ('duracion', models.IntegerField()),
                ('epigrafe', models.CharField(max_length=100)),
            ],
        ),
    ]