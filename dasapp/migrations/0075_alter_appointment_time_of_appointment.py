# Generated by Django 4.1.13 on 2024-10-27 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0074_alter_appointment_time_of_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time_of_appointment',
            field=models.CharField(blank=True, choices=[('09:00 AM', '09:00 AM'), ('10:00 AM', '10:00 AM'), ('11:00 AM', '11:00 AM'), ('12:00 PM', '12:00 PM'), ('01:00 PM', '01:00 PM'), ('02:00 PM', '02:00 PM'), ('03:00 PM', '03:00 PM'), ('04:00 PM', '04:00 PM'), ('05:00 PM', '05:00 PM')], max_length=20),
        ),
    ]
