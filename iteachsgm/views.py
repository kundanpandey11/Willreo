from django.forms import models
from django.shortcuts import render, redirect
from .models import upload
from .forms import uploadForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from accounts.models import CustomUserAccounts


# from pybase64 import b64decode

# Create your views here.

def upload_page(request):
    form = uploadForm()
    # image = form.cleaned_data['image']
    # b64_img = b64encode(image.file.read())
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            form.save()
            return redirect('main')  
    else:
        form = uploadForm()

    return render(request, 'upload.html', {'form': form} )



def main(request):
    
    loads = upload.objects.all()

    return render(request, 'main_page.html', {'loads': loads})


class HomeView(LoginRequiredMixin ,ListView):
    template_name = 'main_page_stu.html'
    queryset = upload.objects.all()
    context_object_name  = 'loads'
    paginate_by = 30  



class ProfileView(ListView):
    template_name = 'profile.html'
    model = CustomUserAccounts



class HelpView(ListView):
    template_name = 'help.html'
    queryset = CustomUserAccounts.objects.filter(is_superuser=False, email__contains='kundan')
    context_object_name = 'allusers'
    




