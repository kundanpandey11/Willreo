from django.urls import path
from . import views


urlpatterns = [
    path('stu/', views.main, name='main'),
    path('tea/', views.HomeView.as_view(), name='main_stu'),
    path('upload/', views.upload_page, name='upload'),
    path('help/', views.HelpView.as_view(), name='help'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('likes/', views.upload_likes, name='upload-likes'),
    path('upload/<pk>/delete/', views.DeletingUpload.as_view(), name='delete'),
    
    

    ]

