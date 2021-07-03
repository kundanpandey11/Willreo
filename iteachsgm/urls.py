from django.urls import path
from . import views

urlpatterns = [
    path('tea/', views.main, name='main'),
    path('stu/', views.HomeView.as_view(), name='main_stu'),
    path('upload', views.upload_page, name='upload'),
    path('help/', views.HelpView.as_view(), name='help'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    ]

