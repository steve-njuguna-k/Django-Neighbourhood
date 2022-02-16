from Neighbourhood import views
from django.urls import path

urlpatterns = [
    path('', views.Home, name='Home')
]
