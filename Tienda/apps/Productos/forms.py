from django import forms
from django.forms import ModelForm
from .models import *
class fproducto(ModelForm):
	class Meta:
		model=Producto