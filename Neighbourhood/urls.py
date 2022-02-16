from Neighbourhood import views
from django.urls import path
from django.conf.urls.static import static
from Core import settings

urlpatterns = [
    path('', views.Home, name="Home"),
    path('register', views.Register, name="Register"),
    path('login', views.Login, name="Login"),
    path('logout', views.Logout, name="Logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)