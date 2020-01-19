from django import forms

ITEM_QUANTITY = [(i, str(i)) for i in range(1,11)]

class AddItemForm(forms.Form):
    """
    Class responsible for creating form to adding item to the basket
    quantity - let user to choose number of item from 1 to 10, coerce is paring to the int
    update - let user to choose if the number of item should be add to the existence one or replace them
    """
    quantity = forms.TypedChoiceField(choices=ITEM_QUANTITY, coerce=int)
    refresh = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
