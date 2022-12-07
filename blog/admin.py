#PARA QUE APAREZCA EN URL ADMIN
from django.contrib import admin

# Importamos el proyecto de blog
from blog.models import *
admin.site.register(Proyecto)
admin.site.register(Tarea)