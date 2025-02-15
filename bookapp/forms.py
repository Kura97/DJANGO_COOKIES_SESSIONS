from django import forms
from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']
