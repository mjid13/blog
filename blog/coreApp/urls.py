from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]