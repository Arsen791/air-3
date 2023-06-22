from django.contrib import admin
from .models import Orders, Details, Shipping, ShippingDetails, Airports, PickupAddress


admin.site.register(Orders)
admin.site.register(Details)
admin.site.register(ShippingDetails)
admin.site.register(Shipping)
admin.site.register(Airports)
admin.site.register(PickupAddress)