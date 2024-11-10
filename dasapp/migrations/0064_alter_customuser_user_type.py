# Generated by Django 4.1.13 on 2024-10-26 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0063_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'admin'), (2, 'doc')], default=1, max_length=50),
        ),
    ]
