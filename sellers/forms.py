from django import forms
from shopping.models import products, category, type, prod_size


class add_type_form(forms.ModelForm):
    class Meta:
        model=type
        fields='__all__'

class add_size_form(forms.ModelForm):
    class Meta:
        model=prod_size
        fields=['size','stock']

class add_item_form(forms.ModelForm):
    class Meta:
        model=products
        fields='__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['type'].queryset = category.objects.none()

            if 'category' in self.data:
                try:
                    category_id = int(self.data.get('category'))
                    self.fields['type'].queryset = category.objects.filter(category_id=category_id).order_by('name')
                except (ValueError, TypeError):
                    print("value error")  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['type'].queryset = self.instance.category.type_set.order_by('name')