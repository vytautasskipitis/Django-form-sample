from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CustomerMessageForm, name='form_insert'),
    path('<int:id>/', views.CustomerMessageForm, name='form_update'),
    path('delete/<int:id>/', views.CustomerMessageDelete, name='form_delete'),
    path('list/', views.CustomerMessageList, name='form_list'),
]


