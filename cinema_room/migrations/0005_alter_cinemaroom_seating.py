# Generated by Django 3.2.4 on 2021-06-26 19:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_room', '0004_alter_cinemaroom_seating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinemaroom',
            name='seating',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.BooleanField(blank=True), size=10), blank=True, size=10),
        ),
    ]