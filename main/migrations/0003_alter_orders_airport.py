# Generated by Django 4.1.2 on 2023-06-14 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_pickupaddress_airport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='airport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airport', to='main.airports'),
        ),
    ]