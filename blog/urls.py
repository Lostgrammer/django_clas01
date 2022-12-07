from django.urls import path
from . import views
#creamos este script para la funcion index de views
urlpatterns = [
    path('nueva/', views.index)
]