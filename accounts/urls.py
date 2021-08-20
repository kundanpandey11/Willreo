from django.urls import path, include
from .views import  landing_page, UpdateProfile


urlpatterns = [
    path('', landing_page.as_view(), name='landing'),
    path('Updateprofile/<str:pk>/', UpdateProfile.as_view(), name='update_profile'),


]
