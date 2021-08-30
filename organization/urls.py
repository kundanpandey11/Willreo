from django.urls import  path
from . import views

urlpatterns = [
    path('', views.create_organization, name='create-organization'),
    path('joining/', views.join_oganization, name='join-organization' ),
]