from django import forms
from django.forms import ModelForm
from .models import *
class fproducto(ModelForm):
	class Meta:
		model=Producto
		fields=("Nombre","Descripcion","Precio","Stock")
class fpedido(ModelForm):
	lista_producto=forms.ModelMultipleChoiceField(queryset=Producto.objects.all(),widget=forms.CheckboxSelectMultiple())
	class Meta:
		model=Pedido 
		exclude=["Fecha_compra"]