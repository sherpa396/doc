# Generated by Django 4.1.13 on 2024-10-23 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0030_appointment_address_appointment_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'admin'), (2, 'doc')], default=1, max_length=50),
        ),
    ]
