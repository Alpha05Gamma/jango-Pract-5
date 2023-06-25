from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    
    
    path('MelinasPage/', views.MelinasPage, name="Melina"),
    path('AstelPage/', views.AstelPage, name="Astel"),
    path('FirePotPage/', views.FirePotPage, name="FirePot"),
    path('WeaponPage/', views.WeaponPage, name="Weapon"),
    path('Home/', views.index, name="home"),

    
]
