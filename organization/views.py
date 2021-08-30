from django.shortcuts import render, reverse, redirect
from django.views.generic import CreateView
from django.contrib import messages
from .forms import CreateOrganizationForm
from django.contrib.auth.decorators import login_required




@login_required
def create_organization(request):
    form = CreateOrganizationForm()
    if request.method == 'POST':
        form = CreateOrganizationForm(request.POST)
        if form.is_valid():
            uform = form.save(commit=False)
            uform.organization_creator = request.user
            uform.save()
            return redirect('main')
        else:
            return render(request, "landing_page.html")
    return render(request, 'create_organization.html', {'form': form})

@login_required
def join_oganization(request, pk):
    return redirect('main')



