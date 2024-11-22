from django.urls import path
from . import views

urlpatterns = [
    path('pessoa/', views.obter_todas_pessoas),
    path('produto/', views.obter_todos_produtos),

]
