from django.shortcuts import render,render_to_response,get_object_or_404
from django.template import RequestContext
from .models import *
from .forms import *
# Create your views here.
def principal(request):
	return render_to_response("principal.html",{},RequestContext(request))
def registrar_producto(request):
	if request.method=="POST":
		form=fproducto(request.POST)
		if form.is_valid():
			form.save()
	form=fproducto()
	return render_to_response("registrarproducto.html",{"form":form},RequestContext(request))
def listar_productos(request):
	lista=Producto.objects.all().order_by("Nombre")
	return render_to_response("listarproductos.html",{"lista":lista},RequestContext(request))
def verproductos(request):
	lista=Producto.objects.all().order_by("Nombre")
	return render_to_response("verproductos.html",{"lista":lista},RequestContext(request))
def detalleproducto(request,id):
	prod=get_object_or_404(Producto,pk=id)
	return render_to_response("verproducto.html",{"prod":prod},RequestContext(request))
def elegirproductomodificar(request):
	lista=Producto.objects.all().order_by("Nombre")
	return render_to_response("elegirproductomod.html",{"lista":lista},RequestContext(request))
def modificar_producto(request,id):
 	prod=get_object_or_404(Producto,pk=id)
 	if request.method=="POST":
 		form=fproducto(request.POST,instance=prod)
 		if form.is_valid():
 			form.save()
 	else:
 		form=fproducto(instance=prod)
 	return render_to_response("modificarproducto.html",{"form":form},RequestContext(request))