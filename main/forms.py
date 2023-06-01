from datetime import date
from django import forms
from django.core.validators import MinValueValidator
from .models import ShipToAddress,PickupAddress, Airports


class ContractsForm(forms.Form):
    supplier_code = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'contr'}))
    reg_num = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'contr'}))
    pot_num = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'contr'}))

class ShipToAddressForm(forms.ModelForm):
    class Meta:
        model = ShipToAddress
        fields = ['dictionaries', 'supplier_code', 'country', 'city', 'street', 'number', 'phone', 'contact_person', 'email', 'airport']

class PickupAddressForm(forms.ModelForm):
    class Meta:
        model = PickupAddress
        fields = ['dictionaries', 'supplier_code', 'country', 'city', 'street', 'number', 'phone', 'contact_person', 'email', 'airport']

class AirportsForm(forms.ModelForm):
    class Meta:
        model = Airports
        fields = ['dictionaries', 'code', 'airport_name', 'type']


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

    DeliveryCountry = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle',
        'placeholder': '',
        'id': 'text-3f76',
        'min': '1',
        'value': '1',
        'step': '1',
    }))

    ShippingDate = forms.DateField(widget=forms.SelectDateWidget(attrs={
        'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle',
        'placeholder': 'ММ/ДД/ГГ',
        'id': 'date-0756',
        'data - date - format': 'mm/dd/yyyy',
        'required': '',
    }),
        validators=[MinValueValidator(limit_value=date.today())]
    )






