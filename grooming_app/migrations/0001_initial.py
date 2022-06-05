# Generated by Django 4.0.4 on 2022-06-01 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Imię')),
                ('surname', models.CharField(max_length=64, verbose_name='Nazwisko')),
                ('e_mail', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('age', models.IntegerField()),
                ('clients', models.ManyToManyField(to='grooming_app.clients')),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Imię')),
                ('surname', models.CharField(max_length=64, verbose_name='Nazwisko')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=64)),
                ('price', models.FloatField()),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grooming_app.dogs')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grooming_app.dogs')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grooming_app.employees')),
            ],
        ),
    ]
