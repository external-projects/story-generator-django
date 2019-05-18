from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name='home'),
    path('execute/', views.execute, name='execute'),
    path('generate/', views.generate, name='generate'),
    path('append/', views.append, name='append'),
]