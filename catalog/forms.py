from crispy_forms.layout import Submit
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper

from catalog.models import Product, Category, Version


class ProductCreateForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price_per_unit')

    def clean_name(self):
        name = self.cleaned_data['name']
        banned_words = ['casino', 'cryptocurrency', 'crypto', 'exchange', 'cheap',
                        'free', 'scam', 'police', 'radar']

        for word in banned_words:
            if word.lower() in name.lower():
                raise ValidationError(f"Слово '{word}' запрещено использовать в названии продукта. ")

        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        banned_words = ['casino', 'cryptocurrency', 'crypto', 'exchange', 'cheap',
                        'free', 'scam', 'police', 'radar']

        for word in banned_words:
            if word.lower() in description.lower():
                raise ValidationError(f"Слово '{word}' запрещено использовать в описании продукта.")

        return description

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super().form_valid(form)

    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

        self.helper.attrs = {'class': 'form-control'}
        self.fields['name'].widget.attrs.update({'placeholder': 'Enter name'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Enter description'})
        self.fields['category'].widget.attrs.update({'placeholder': 'Choose category'})
        self.fields['image'].widget.attrs.update({'placeholder': 'Upload photo'})
        self.fields['price_per_unit'].widget.attrs.update({'placeholder': 'Enter price'})


class ProductUpdateForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price_per_unit')


class VersionCreateForm(ModelForm):
    class Meta:
        model = Version
        fields = ('version_name', 'version_number', 'current_version')

    def __init__(self, *args, **kwargs):
        super(VersionCreateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

        self.helper.attrs = {'class': 'form-control'}
        self.fields['version_name'].widget.attrs.update({'placeholder': 'Enter name'})
        self.fields['version_number'].widget.attrs.update({'placeholder': 'Enter number'})
        self.fields['current_version'].widget.attrs.update({'placeholder': 'Choose version'})


class VersionUpdateForm(ModelForm):
    class Meta:
        model = Version
        fields = ('version_name', 'version_number', 'current_version')
