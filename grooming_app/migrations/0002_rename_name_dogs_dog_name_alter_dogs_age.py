# Generated by Django 4.0.4 on 2022-06-02 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grooming_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dogs',
            old_name='name',
            new_name='dog_name',
        ),
        migrations.AlterField(
            model_name='dogs',
            name='age',
            field=models.FloatField(verbose_name='wiek'),
        ),
    ]