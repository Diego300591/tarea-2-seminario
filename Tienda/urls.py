from django.conf.urls import patterns, include, url
from django.contrib import admin
from Tienda.apps.Productos.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Tienda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',principal),
    url(r'^registrarprod/',registrar_producto),
    url(r'^listaprod/',listar_productos),
    url(r'^vertodosprod/',verproductos),
    url(r'^elegirprodmodificar/',elegirproductomodificar),
    url(r'^verdetallesprod/(?P<id>\d+)/$',detalleproducto,name='detalleproducto'),
    url(r'^modificarprod/(?P<id>\d+)/$',modificar_producto,name='modificar_producto'),
)