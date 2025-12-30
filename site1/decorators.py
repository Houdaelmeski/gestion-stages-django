
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import *


def notLogedUser(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
        return wrapper_func
    
def allowedUsers(allowedUsers=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group in allowedUsers:
                    return view_func(request, *args, **kwargs)
                else:
                    cat2=Encadrent.objects.get(user=request.user)
                 
                    return redirect('encadrant' , cat2.id)
            else:
                cat2= Stagiaire.objects.get(user=request.user)
                return redirect('stagiaire' , cat2.id)
                

        return wrapper_func
    return decorator


    