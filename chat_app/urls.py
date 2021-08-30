from django.urls import path
from .views import hello

app_name = 'chat_app'

urlpatterns = [
        path('', hello, name='hello'),
]