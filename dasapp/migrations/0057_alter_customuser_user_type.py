# Generated by Django 4.1.13 on 2024-10-25 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0056_alter_payment_cardnumbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'doc'), (1, 'admin')], default=1, max_length=50),
        ),
    ]
