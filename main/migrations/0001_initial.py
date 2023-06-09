# Generated by Django 4.1.2 on 2023-06-14 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airports',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=100)),
                ('airport_name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('INT', 'Международные'), ('EAEU', 'Аэропорты стран Таможенного союза'), ('LOCAL', 'Внутренние аэропорты')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DetailName', models.CharField(max_length=100, verbose_name='Detail Name')),
                ('Count', models.IntegerField(verbose_name='Count of details')),
                ('DeliveryCountry', models.CharField(max_length=100, verbose_name='Delivery Country')),
            ],
        ),
        migrations.CreateModel(
            name='PickupAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_code', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('contact_person', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('airport', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DetailName', models.CharField(max_length=100, verbose_name='Detail Name')),
                ('Count', models.IntegerField(verbose_name='Count of details')),
            ],
        ),
        migrations.CreateModel(
            name='ShipToAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_code', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('contact_person', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('airport', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShippingName', models.CharField(max_length=50, verbose_name='Name of Shipping')),
                ('Details', models.ManyToManyField(to='main.shippingdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderName', models.IntegerField(verbose_name='Name of order')),
                ('OrderDate', models.DateField(verbose_name='Date when order came')),
                ('Details', models.ManyToManyField(to='main.details')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='main.pickupaddress')),
                ('airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airports', to='main.airports')),
            ],
        ),
    ]
