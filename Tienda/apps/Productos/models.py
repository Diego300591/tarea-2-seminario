from django.db import models
# Create your models here.
class Producto(models.Model):
	Nombre=models.CharField(max_length=100)
	Descripcion=models.TextField()
	Precio=models.PositiveIntegerField(default=0)
	Stock=models.PositiveIntegerField(default=0)
	def __unicode__(self):
		return self.Nombre
class Pedido(models.Model):
	Cliente=models.CharField(max_length=100)
	lista_producto=models.ManyToManyField(Producto,blank=False)
	Fecha_compra=models.DateField(auto_now=True)
	Estado=models.BooleanField(default=False)
