from django import forms
from .models import Book, Patron, Borrow
from django.forms import DateInput  

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class PatronForm(forms.ModelForm):
    class Meta:
        model = Patron
        fields = ['first_name', 'last_name', 'email']

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['patron', 'book', 'borrow_date', 'return_date']
        widgets = {
            'borrow_date': DateInput(attrs={'type': 'date'}),
            'return_date': DateInput(attrs={'type': 'date'}),
        }
