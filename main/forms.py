from datetime import date
from django import forms
from django.core.validators import MinValueValidator
from .models import ShipToAddress,PickupAddress, Airports



class ShipToAddressForm(forms.ModelForm):
    class Meta:
        model = ShipToAddress
        fields = [ 'supplier_code', 'country', 'city', 'street', 'number', 'phone', 'contact_person', 'email', 'airport']

class PickupAddressForm(forms.ModelForm):
    class Meta:
        model = PickupAddress
        fields = [ 'supplier_code', 'country', 'city', 'street', 'number', 'phone', 'contact_person', 'email']

class AirportsForm(forms.ModelForm):
    class Meta:
        model = Airports
        fields = [ 'code', 'airport_name', 'type']


class OrdersForm(forms.Form):
    OrderName = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': '',
        'id': 'id_OrderName',
        'min': '1',
        'value': '1',
        'step': '1',
    }))
    DetailName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': '',
        'id': 'id_DetailName',
        'style': 'width: 100px',
    }))
    Count = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': '',
        'id': 'id_Count',
        'min': '1',
        'value': '1',
        'step': '1',
        'style': 'width: 50px',
    }))
    DeliveryCountry = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': '',
        'id': 'id_DeliveryCountry',
        'style': 'width: 100px',
    }))

    OrderDate = forms.DateField(
        required=True,
        widget=forms.widgets.DateInput(
            attrs={
                "placeholder": "",
                "type": "date",
                "class": "form-control",
                "id": "id_OrderDate",
            }
        ),
        label="",
    )

    # Поля из PickupAddressForm
    supplier_code = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': '',
        'id': 'id_supplier_code',
        'style': 'width: 100px',
    }))
    country = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': '',
        'id': 'id_country',
        'style': 'width: 100px',
    }))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': '',
        'id': 'id_city',
        'style': 'width: 100px',
    }))
    street = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': '',
        'id': 'id_street',
        'style': 'width: 100px',
    }))
    number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '',
        'id': 'id_number',

        'style': 'width: 100px',
    }))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': '',
        'id': 'id_phone',
        'style': 'width: 100px',
    }))
    contact_person = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': '',
        'id': 'id_contact_person',
        'style': 'width: 100px',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': '',
        'id': 'id_email',
        'style': 'width: 100px',
    }))

    # Поля из AirportsForm
    code = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': '',
        'id': 'id_code',
        'style': 'width: 100px',
    }))
    airport_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': '',
        'id': 'id_airport_name',
        'style': 'width: 100px',
    }))
    TYPE_CHOICES = [
    ('INT', 'Международные'),
    ('EAEU', 'Аэропорты стран Таможенного союза'),
    ('LOCAL', 'Внутренние аэропорты'),
]
    type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.Select(attrs={
        'id': 'id_type',
        'style': 'width: 100px',
    }))



class DetailForm(forms.Form):
    DetailName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle',
        'placeholder': 'Название Детали',
        'id': 'id_DetailName',
    }))
    Count = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle',
        'placeholder': '',
        'id': 'id_Count',
        'min': '1',
        'value': '1',
        'step': '1',
    }))
    DeliveryCountry = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle',
        'placeholder': 'Страна поставки',
        'id': 'id_DeliveryCountry',
    }))


class ShippingForm(forms.Form):
    ShippingName = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle',
        'placeholder': '',
        'id': 'name-6797',
        'label': 'name',
        'min': '1',
        'value': '1',
        'step': '1',
    }))







