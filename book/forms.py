from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User
from django.forms import ModelForm


class createuserform(UserCreationForm):
    class Meta:
        models = User
        fields = ['username', 'password']


class createcustomerform(ModelForm):
    class Meta:
        models = Customer
        fields = '_all_'


class createbookform(ModelForm):
    class Meta:
        models = Book
        fields = '_all_'
