# Generated by Django 4.1.13 on 2024-10-24 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0034_alter_payment_cardnumbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='cardnumbers',
            field=models.CharField(max_length=255, null=True),
        ),
    ]