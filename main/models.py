from django.db import models

class Dictionaries(models.Model):
    pass

class Contracts(models.Model):
    dictionaries = models.ForeignKey(Dictionaries, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    supplier_code = models.CharField(max_length=100, null=False)
    reg_num = models.CharField(max_length=100, null=False)
    pot_num = models.CharField(max_length=100, null=False)

    
class ShipToAddress(models.Model):
    dictionaries = models.ForeignKey(Dictionaries, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    supplier_code = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)
    street = models.CharField(max_length=100, null=False)
    number = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)
    contact_person = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    airport = models.CharField(max_length=100, null=False)

class PickupAddress(models.Model):
    dictionaries = models.ForeignKey(Dictionaries, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    supplier_code = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)
    street = models.CharField(max_length=100, null=False)
    number = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)
    contact_person = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    airport = models.CharField(max_length=100, null=False)


class Airports(models.Model):
    dictionaries = models.ForeignKey(Dictionaries, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100, null=False)
    airport_name = models.CharField(max_length=100, null=False)
    TYPE_CHOICES = [
        ('INT', 'Международные'),
        ('EAEU', 'Аэропорты стран Таможенного союза'),
        ('LOCAL', 'Внутренние аэропорты'),
    ]
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)



class Details(models.Model):
    DetailName = models.CharField('Detail Name', max_length=100)
    Count = models.IntegerField('Count of details')
    DeliveryCountry = models.CharField('Delivery Country', max_length=100)


class Orders(models.Model):
    OrderName = models.CharField('Name of order', max_length=50)
    OrderDate = models.DateField('Date when order came')
    Details = models.ManyToManyField(Details)


class ShippingDetails(models.Model):
    DetailName = models.CharField('Detail Name', max_length=100)
    Count = models.IntegerField('Count of details')

class Shipping(models.Model):
    ShippingName = models.CharField('Name of Shipping', max_length=50)
    Details = models.ManyToManyField(ShippingDetails)


