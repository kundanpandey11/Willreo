from .models import CustomUserAccounts
from .forms import RegistrationForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, UpdateView
from django.urls import reverse
from .forms import AddForm
from django.contrib.auth.mixins import LoginRequiredMixin
# from iteachsgm.views import Profile


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
            
                

class landing_page(TemplateView):
    template_name = 'landing_page.html'

           
class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = CustomUserAccounts
    form_class = AddForm
    template_name = 'registration/update_profile.html'
    success_url = '/mainpage/profile/'

    # def get_context_data(self, **kwargs):
    #     context = super(UpdateProfile, self).get_context_data(**kwargs)
    #     context['pk'] = self.objects.filter(id=self.id)# Whatever you want to add here (e.g. self.object.artist_id)
    #     return context

    # def get_success_url(self):
        # return reverse('profile')

 

    