# Generated by Django 4.1.2 on 2023-06-14 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_orders_airport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='address',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='airport',
            new_name='Airport',
        ),
    ]
