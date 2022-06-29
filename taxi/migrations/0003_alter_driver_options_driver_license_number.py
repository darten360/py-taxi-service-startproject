# Generated by Django 4.0.5 on 2022-06-29 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_alter_car_options_alter_driver_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ['username'], 'verbose_name': ['Driver'], 'verbose_name_plural': ['Drivers']},
        ),
        migrations.AddField(
            model_name='driver',
            name='license_number',
            field=models.CharField(blank=True, max_length=63, null=True, unique=True),
        ),
    ]