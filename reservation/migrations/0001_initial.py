# Generated by Django 3.2.4 on 2021-06-27 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cinema_room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('armored_row', models.IntegerField()),
                ('armored_chair', models.IntegerField()),
                ('cinema_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_room.cinemaroom')),
            ],
        ),
    ]
