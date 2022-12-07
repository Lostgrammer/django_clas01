from django.db import models

# los modelos se convierten en tablas
class Proyecto (models.Model):
    #columnas y tipos de datos
    nombre = models.CharField(max_length=200)
    caracteristica = models.CharField(max_length=300)
