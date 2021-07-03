from django.shortcuts import render, redirect 
from .models import CustomUserAccounts
from .forms import UserCreationForm, RegistrationForm
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.contrib.auth import login as auth_login
from django.urls import reverse



class RegistrationView(CreateView):
    model = CustomUserAccounts
    template_name = 'registration/register.html'
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += '?next{}'.format(next_url)
        return success_url
            
                

# class HomeView(ListView):
#     template_name = 'main_page_stu.html'
#     queryset = Upload.objects.filter(flagged=False)
#     context_object_name  = 'listings'
#     paginate_by = 30   

           
            
            
                    

 

    