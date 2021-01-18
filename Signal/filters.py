
import django_filters
from .models import *
from django_filters import CharFilter
from django import forms

class mainFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    description = CharFilter(field_name='description', lookup_expr='icontains')
    class Meta:
        model = Signal
        fields = '__all__'
        exclude = ['image']

        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
        }

