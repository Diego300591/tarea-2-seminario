from django import forms
from django.forms import ModelForm
from .models import *
class fproducto(ModelForm):
	class Meta:
		model=Producto
class fpedido(ModelForm):
	class Meta:
		model=Pedido