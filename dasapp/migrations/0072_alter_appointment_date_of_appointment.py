# Generated by Django 4.1.13 on 2024-10-27 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0071_alter_appointment_date_of_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date_of_appointment',
            field=models.TextField(blank=True),
        ),
    ]