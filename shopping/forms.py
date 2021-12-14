from django import forms
from .models import products, category


class add_item_form(forms.ModelForm):
    class Meta:
        model = products
        fields = '__all__'


