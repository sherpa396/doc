# Generated by Django 4.1.13 on 2024-10-24 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0051_alter_customuser_user_type_alter_payment_cardnumbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='cardnumbers',
            field=models.BigIntegerField(blank=True),
        ),
    ]
