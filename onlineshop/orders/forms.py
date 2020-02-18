from django import forms
from .models import Order
from localflavor.pl.forms import PLPostalCodeField, PLNIPField

class OrderForm(forms.ModelForm):
    """
        code = PLPostalCodeField()
            A form field that validates as Polish postal code.
            Valid code is XX-XXX where X is digit.
        nip = PLNIPField()
            A form field that validates as Polish Tax Number (NIP).
            Valid forms are: XXX-YYY-YY-YY, XXX-YY-YY-YYY or XXXYYYYYYY.
            Field validation with localflavor module
    """
    class Meta:
        model = Order
        code = PLPostalCodeField()
        nip = PLNIPField()
        fields = ['name', 'surname', 'email', 'street', 'street_number', 'city', 'code', 'nip']