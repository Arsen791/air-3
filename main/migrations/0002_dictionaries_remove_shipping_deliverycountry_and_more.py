# Generated by Django 4.1.2 on 2023-06-03 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionaries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='DeliveryCountry',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='ShippingDate',
        ),
        migrations.AlterField(
            model_name='shipping',
            name='ShippingName',
            field=models.CharField(max_length=50, verbose_name='Name of Shipping'),
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
                ('dictionaries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dictionaries')),
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
                ('dictionaries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dictionaries')),
            ],
        ),
        migrations.CreateModel(
            name='Contracts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_code', models.CharField(max_length=100)),
                ('reg_num', models.CharField(max_length=100)),
                ('pot_num', models.CharField(max_length=100)),
                ('dictionaries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dictionaries')),
            ],
        ),
        migrations.CreateModel(
            name='Airports',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=100)),
                ('airport_name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('INT', 'Международные'), ('EAEU', 'Аэропорты стран Таможенного союза'), ('LOCAL', 'Внутренние аэропорты')], max_length=100)),
                ('dictionaries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dictionaries')),
            ],
        ),
    ]
