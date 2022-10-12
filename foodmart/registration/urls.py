from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('contact/',views.contact),
    path('signup/', views.signup),
    path('signin/', views.signin),
]