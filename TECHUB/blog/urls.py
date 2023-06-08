from django.urls import path

from . import views



urlpatterns = [
    path('', views.home, name='home'),    
    path('about/', views.about, name='about'),    
    path('contact/', views.contact, name='contact'),    
    path('login/', views.login, name='login'),    
    path('update_profile/', views.update_profile, name='update_profile'),    
    path('update_address/', views.update_address, name='update_address'),    
    path('test/', views.test, name='test'),    
    path('register/', views.register, name='register'),    
    path('signup/', views.signup, name='signup'),    
    path('team/', views.team, name='team'),    
    path('profile/', views.profile, name='profile'),    
]
