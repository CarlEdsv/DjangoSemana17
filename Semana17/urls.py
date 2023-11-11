from django.contrib import admin
from django.urls import path
from Universidad.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',carreraList),
    #path('',profesorList),
    #path('',estudianteList),
    path('',asignaturaList)#Añadimos directamente la view (lo recomendable es crear una lista de urls en la app)
]

