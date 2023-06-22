# Generated by Django 4.1.2 on 2023-06-14 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_orders_address_alter_orders_airport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='Airport',
        ),
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='main.pickupaddress'),
        ),
        migrations.AddField(
            model_name='orders',
            name='airport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='airport', to='main.airports'),
        ),
    ]
