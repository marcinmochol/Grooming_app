# Generated by Django 4.0.4 on 2022-06-06 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grooming_app', '0006_alter_dogs_age_alter_dogs_breed_alter_dogs_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='dog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='grooming_app.dogs'),
        ),
    ]