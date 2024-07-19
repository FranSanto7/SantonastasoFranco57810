from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('auto/<int:id>/', views.auto_detail, name='auto_detail'),
    path('auto/create/', views.auto_create, name='auto_create'),
    path('auto/<int:id>/edit/', views.auto_edit, name='auto_edit'),
    path('auto/<int:id>/delete/', views.auto_delete, name='auto_delete'),
    path('buscar/', views.buscar_autos, name='buscar_autos'),
]