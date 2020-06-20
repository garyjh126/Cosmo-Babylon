from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import View, FormView, CreateView

from contacts.forms import ContactForm
from django.http import JsonResponse, HttpResponse
from .models import Message

import re

def home_view(request):
    if request.method == "POST": # Sent from template towards server.
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            form = ContactForm()

    else: # Create blank form for user to see on first sight
        
        form = ContactForm()

    return render(request, "pages/home.html", {'form': form })

def validate_email(request):
    email = request.GET.get('email', None)

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    email_status = {
        'is_valid': True if re.search(regex,email) else False
    }

    
    return JsonResponse(email_status)

def validate_form(request):
    name = request.GET.get('name', None)
    message = request.GET.get('message', None)

    if name and message:
        return JsonResponse({
            "is_valid": True
        })
    else:
        return JsonResponse({
            "is_valid": False
        })
        


