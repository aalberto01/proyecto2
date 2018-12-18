from django.urls import path
from .views import registros,archivo

app_name = "archivo"

urlpatterns = [
    path('registros/', registros.as_view()),
    path('nuevoarchivo/', archivo.as_view()),
]