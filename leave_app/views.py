from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import leave_form
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'home.html')

@login_required
def dashboard(request):
    return render(request,'dashboard.html')


@login_required
def leave(request):    
    if request.method == 'POST':
        form = leave_form(request.POST)
    # check whether it's valid:
        if form.is_valid():
            
            # process the data in form.cleaned_data as required
            
            p = form.save(commit=False)
            p.employee = request.user
            data = leave_model.objects.all()
            p.save()
            return render(request,'status.html',{'data':data})
            # '''
            # redirect to a new URL:
        # if a GET (or any other method) we'll create a blank form    
    else:
        form = leave_form()
       
    return render(request,'leave.html',{'form':form})

@login_required
def leave_stat(request):
    form = leave_form()
    a = leave_model.objects.filter(employee=request.user)
    args = {'form':form,'a':a}
    return render(request,'status.html',args)
