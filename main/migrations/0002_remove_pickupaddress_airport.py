# Generated by Django 4.1.2 on 2023-06-14 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pickupaddress',
            name='airport',
        ),
    ]
