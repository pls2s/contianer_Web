from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ),
    path('login',views.login),
    path('register',views.register),
    path('infomation',views.infomation),
    path('production',views.production)
]