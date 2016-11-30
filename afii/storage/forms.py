from django import forms
from storage.models import Category


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['storage', 'name', 'is_base', 'base_category']
        required_css_class = 'form-control'

    def __init__(self, *args, **kwargs):
        super(AddCategoryForm, self).__init__(*args, **kwargs)
        # adding css classes to widgets without define the fields:
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'