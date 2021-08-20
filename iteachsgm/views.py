from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import DeleteView
from .models import upload
from .forms import uploadForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import UpdateView, TemplateView
from accounts.models import CustomUserAccounts
from accounts.forms import UserChangeForm, AddForm
from django.http import HttpResponseRedirect
from django.conf import settings


# from pybase64 import b64decode
def upload_likes(request):
    user = request.user    
    if request.method == 'POST':
        upload_id = request.POST.get('upload_id')
        scroll_id = request.POST.get('scroll_id')
        upload_managing_likes = upload.objects.get(id=upload_id)
        

        if user not in upload_managing_likes.likes.all():
            upload_managing_likes.likes.add(user)
        else:
            upload_managing_likes.likes.remove(user)


        return HttpResponseRedirect(reverse('main'))



# def upload_likes(request):
#     user = request.user
#     upload_managing_likes = get_object_or_404(upload, id=request.POST.get('upload_id'))



def upload_page(request):
    form = uploadForm()
    user = request.user
    context = {'user':user, 'form':form}
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)        
        if form.is_valid():          
            form_record = form.save(commit=False)
            form_record.creator = request.user
            form_record.save()
            return redirect('main') 
        else:
            form = uploadForm()
    return render(request, 'upload.html', context)



def main(request):    
    loads = upload.objects.all()
    user = request.user
    context = {'loads':loads, 'user':user}
    if DeletingUpload():
        return render(request, 'main_page.html', context)
    else:
        return render(request, 'main_page.html', context)


class HomeView(LoginRequiredMixin ,ListView):
    template_name = 'main_page.html'
    queryset = upload.objects.all()
    context_object_name  = 'loads'
    paginate_by = 30  




class ProfileView(ListView):
    template_name = 'profile.html'
    model = CustomUserAccounts



class HelpView(ListView):
    template_name = 'help.html'
    queryset = CustomUserAccounts.objects.filter(is_superuser=False, )
    context_object_name = 'allusers'
    

class IndexView(TemplateView):
    template_name = 'index.html'


class  DeletingUpload(DeleteView):
    model = upload
    success_url = '/mainpage/tea'
 


    


