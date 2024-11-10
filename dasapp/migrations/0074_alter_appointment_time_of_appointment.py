# Generated by Django 4.1.13 on 2024-10-27 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0073_alter_appointment_date_of_appointment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time_of_appointment',
            field=models.CharField(blank=True, choices=[('10:00 - 10:30', '10:00 - 10:30'), ('10:30 - 11:00', '10:30 - 11:00'), ('11:00 - 11:30', '11:00 - 11:30'), ('11:30 - 12:00', '11:30 - 12:00'), ('12:00 - 12:30', '12:00 - 12:30'), ('12:30 - 1:00', '12:30 - 1:00'), ('1:00 - 1:30', '1:00 - 1:30'), ('1:30 - 2:00', '1:30 - 2:00'), ('2:00 - 2:30', '2:00 - 2:30'), ('2:30 - 3:00', '2:30 - 3:00'), ('3:00 - 3:30', '3:00 - 3:30'), ('3:30 - 4:00', '3:30 - 4:00')], max_length=20),
        ),
    ]
