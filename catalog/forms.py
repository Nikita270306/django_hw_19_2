from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms

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


class VersionUpdateForm(ModelForm):
    class Meta:
        model = Version
        fields = ('version_name', 'version_number', 'current_version')