# Generated by Django 4.1.13 on 2024-10-24 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0041_alter_customuser_user_type_alter_payment_cardnumbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'doc'), (1, 'admin')], default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='payment',
            name='cardnumbers',
            field=models.BigIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='payment',
            name='expirydate',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
