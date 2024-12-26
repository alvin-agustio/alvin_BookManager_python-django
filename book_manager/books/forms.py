from django import forms
from .models import Book
from django.forms import DateInput
from datetime import date
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'genre', 'summary']
        
    published_date = forms.DateField(
        widget=DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
    )