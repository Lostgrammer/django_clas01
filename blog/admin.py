#PARA QUE APAREZCA EN URL ADMIN
from django.contrib import admin

# Importamos el proyecto de blog
from blog.models import Proyecto
admin.site.register(Proyecto)