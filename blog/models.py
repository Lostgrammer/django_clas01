from django.db import models

# los modelos se convierten en tablas
class Proyecto (models.Model):
    #columnas y tipos de datos
    nombre = models.CharField(max_length=200)
    caracteristica = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre+' -> '+self.caracteristica

class Tarea (models.Model):
    nombre = models.CharField(max_length=100)
    proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE) #llave foranea con borrado forma cascada
    def __str__(self):
        return self.nombre +' -> Proyecto: ' + self.proyecto.nombre