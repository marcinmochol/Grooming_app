# Generated by Django 4.0.4 on 2022-06-04 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grooming_app', '0005_dogs_breed_dogs_comment_alter_clients_e_mail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogs',
            name='age',
            field=models.FloatField(verbose_name='Wiek'),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='breed',
            field=models.CharField(max_length=128, null=True, verbose_name='Rasa'),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='comment',
            field=models.TextField(null=True, verbose_name='Komentarz'),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='dog_name',
            field=models.CharField(max_length=64, verbose_name='Imię'),
        ),
    ]
