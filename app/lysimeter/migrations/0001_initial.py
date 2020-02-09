# Generated by Django 2.2.3 on 2020-02-09 16:50

from django.db import migrations, models
import djongo.models.fields
import lysimeter.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceParams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lysimeter', models.CharField(max_length=10)),
                ('battery', models.CharField(max_length=10)),
                ('ambient_temperature', models.CharField(max_length=10)),
                ('ambient_humidity', models.CharField(max_length=10)),
                ('ambient_light', models.CharField(max_length=10)),
                ('soil_temperature01', models.CharField(max_length=10)),
                ('soil_temperature02', models.CharField(max_length=10)),
                ('soil_temperature03', models.CharField(max_length=10)),
                ('soil_humidity01', models.CharField(max_length=10)),
                ('soil_humidity02', models.CharField(max_length=10)),
                ('soil_humidity03', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('lysimeter_weight', models.CharField(max_length=10)),
                ('sediment_weight', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=10, null=True)),
                ('timestamp', models.DateTimeField()),
                ('device_params', djongo.models.fields.EmbeddedModelField(model_container=lysimeter.models.DeviceParams, null=True)),
            ],
            options={
                'verbose_name': 'Lysimeter',
                'verbose_name_plural': 'Lysimeters',
            },
        ),
    ]
