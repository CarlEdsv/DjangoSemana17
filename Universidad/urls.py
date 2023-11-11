from django.urls import path
from . import views
urlpatterns = [
#path('', views.index, name='index'),  
#Si dejo la primera parte de la ruta vacía si funciona...
path('', views.list_prov, name='list_prov'),
path('', views.list_prod, name='list_prod'),
path('', views.list_client, name='list_client')
]