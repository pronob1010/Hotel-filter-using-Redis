# Generated by Django 3.2.5 on 2021-07-24 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('hotel_description', models.TextField(max_length=250)),
                ('hotel_image', models.ImageField(upload_to='Hotel')),
                ('chech_in_From', models.TimeField()),
                ('chech_in_To', models.TimeField()),
                ('check_out_From', models.TimeField()),
                ('check_out_To', models.TimeField()),
                ('country', models.CharField(max_length=15)),
                ('zip_code', models.CharField(max_length=10)),
                ('division', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=15)),
                ('street', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('room_image', models.ImageField(upload_to='Rooms')),
                ('price', models.PositiveIntegerField()),
                ('bed_number', models.PositiveIntegerField()),
                ('max_guests_allow', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField(default=0)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.hotels')),
            ],
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('Hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.hotels')),
            ],
        ),
    ]
