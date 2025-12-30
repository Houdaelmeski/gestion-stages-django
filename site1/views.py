from django.shortcuts import render, get_object_or_404,redirect

# Create your views here.
from .forms import *

#just text httpresponce
from django.http import HttpResponse
#import models to ritch the db
from .models import *
from django.urls import path , include
#forms from djangoformess...

#formes...
from django.forms import inlineformset_factory
#filtters..

#autontification django....
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

#view messeges...#message errore sucess...
from django.contrib import messages
#loginnnn....
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as myLogin
#haaaaaaaaaaaaaaaaaaaaaaaaaaaa
from django.contrib.auth.decorators import login_required
#decorators permisions....
from django.db.models import Count
from django.contrib.auth.decorators import permission_required

#recaptchaaaaaaa.......
import requests
from django.conf import settings
from .decorators import *
#payment........
from django.views.generic.base import TemplateView
# def home2(request):
#     return render(request,'site1/home.html')

@login_required(login_url='loginn')
@allowedUsers(allowedUsers=['admin'])
def home1(request):
    stages_without_encadrent = Stage.objects.filter(encadrent__isnull=True)
    encadrents_without_stages = Encadrent.objects.filter(stage__isnull=True).distinct()
    encadrents_with_stages = Encadrent.objects.annotate(num_stages=Count('stage'))
    recent_stagiaires = Stagiaire.objects.order_by('-date_created')[:10]
    cat1= Stage.objects.filter( statusStage="Encours")
    cat2= Encadrent.objects.all()

    context = {
        'stages_without_encadrent': stages_without_encadrent,
        'encadrents_without_stages': encadrents_without_stages,
        'recent_stagiaires': recent_stagiaires,
         'cat1': cat1,
         'cat2': cat2,
    }
    return render(request,'site1/home.html',context)

@login_required(login_url='loginn')
@allowedUsers(allowedUsers=['admin'])
def recherche(request):
    form = SearchForm(request.GET or None)
    stages = Stage.objects.all()

    if form.is_valid():
        nom_stage = form.cleaned_data.get('nom_stage')
        encadrant = form.cleaned_data.get('encadrant')
        stagiaire = form.cleaned_data.get('stagiaire')
        type_stage = form.cleaned_data.get('type_stage')

        if nom_stage:
            stages = stages.filter(nom__icontains=nom_stage)
        if encadrant:
            stages = stages.filter(encadrent__nom__icontains=encadrant)
        if stagiaire:
            stages = stages.filter(stagiaire__nom__icontains=stagiaire)
        if type_stage:
            stages = stages.filter(type=type_stage)

    context = {
        'form': form,
        'stages': stages
    }
    return render(request, 'site1/rechercher.html', context)



@login_required(login_url='loginn')
def stage(request,pk):
    stage=Stage.objects.get(id=pk)
    encadrant=Encadrent.objects.get(id=stage.encadrent.id)
    stagiaire=Stagiaire.objects.get(id=stage.stagiaire.id)
    context = {
        'stage': stage,
        'encadrant': encadrant,
        'stagiaire': stagiaire,
    }
    return render(request,'site1/stage.html',context)

@login_required(login_url='loginn')
@allowedUsers(allowedUsers=['encadrent','admin'])
def encadrant(request,pk):
    encad=Encadrent.objects.get(id=pk)
    cat1= Stage.objects.filter( encadrent=encad)
    context = {
        'encad': encad,
        'cat1': cat1,     
    }
    return render(request,'site1/encad.html',context)

def n_encadrent(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=EncadrentCreatForm()
        if request.method=='POST':
            print(request.POST)
            form=EncadrentCreatForm(request.POST)
            if form.is_valid():
                form.save()
                username=form.cleaned_data.get('username')
                user=User.objects.get(username=username)
                group = Group.objects.get(name='encadrent')
                group.user_set.add(user.id)
                messages.success(request,' Created sucssefuly!')
                return redirect('loginn')
    context={
        'form':form,
    }
    return render(request,'site1/my_encadrent_form.html',context)


@login_required(login_url='loginn')
@allowedUsers(allowedUsers=['encadrent','admin'])
def u_encadrent(request,pk):
    encadrent=Encadrent.objects.get(id=pk)
    form=EncadrentForm(instance=encadrent)
    if request.method=='POST':
        print(request.POST)
        form=EncadrentForm(request.POST,request.FILES,instance=encadrent)
        if form.is_valid():
            form.save()
            return redirect('encadrant',pk)
    context={
        'form':form,
    }
    return render(request,'site1/editerencadrent.html',context)

@login_required(login_url='loginn')
@allowedUsers(allowedUsers=['admin'])
def creeStage(request):
    form=StageForm()
    if request.method=='POST':
        print(request.POST)
        form=StageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form':form,
    }
    return render(request,'site1/creestage.html',context)

@login_required(login_url='login')
@allowedUsers(allowedUsers=['encadrent','admin'])
def edit_stage(request, pk):
    stage = get_object_or_404(Stage, pk=pk)
    form = StageForm(instance=stage)
    if request.method == 'POST':
        form = StageForm(request.POST, instance=stage)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
        'stage': stage,
    }
    return render(request, 'site1/creestage.html', context)

@login_required(login_url='login')
@allowedUsers(allowedUsers=['encadrent','admin'])
def delete_stage(request, pk):
    stage = get_object_or_404(Stage, pk=pk)
    if request.method == 'POST':
        stage.delete()
        return redirect('/')
    context = {
        'stage': stage,
    }
    return render(request, 'site1/delete.html', context)

def loginn(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                myLogin(request,user)
                return redirect('/')
            else:
                messages.info(request,'username or password is incorrect')
    context={
        
    }
    return render(request,'site1/login.html',context)

@login_required(login_url='loginn')
def logoutt(request):
    logout(request)
    return redirect ('loginn')

def registeretud(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=StagiereCreatForm()
        if request.method=='POST':
            print(request.POST)
            form=StagiereCreatForm(request.POST)
            if form.is_valid():
                form.save()
                nom = form.cleaned_data.get('nom')
                messages.success(request,nom+' Created sucssefuly!')
                return redirect('loginn')
    context={
        'form':form,
    }
    return render(request,'site1/registeretud.html',context)

def nnn (request):
    return render(request,'site1/nnn.html')


@login_required(login_url='login')
def u_stagiere(request,pk):
    stagiaire=Stagiaire.objects.get(id=pk)
    form=imgstagiere(request.POST, request.FILES,instance=stagiaire)
    if request.method == 'POST':
            nom=request.POST.get('nom')
            prenom=request.POST.get('prenom')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            niv = request.POST.get('niv')
            age = request.POST.get('age')
            ecole=request.POST.get('ecole')
            form=imgstagiere(request.POST,request.FILES,instance=stagiaire)
            if form.is_valid():
                form.save()
                if email:
                    stagiaire.email = email
                if phone:
                    stagiaire.phone = phone
                if niv:
                    stagiaire.niv = niv
                if age:
                    stagiaire.age = age
                if ecole:
                    stagiaire.ecole = ecole
                if nom:
                    stagiaire.nom = nom
                if prenom:
                    stagiaire.prenom = prenom
                stagiaire.save()
                
                return redirect('stagiaire',pk)
    context = {
            'stagiaire': stagiaire,
            'form':form,
        }
    return render(request,'site1/editer_stagiere.html',context)

@login_required(login_url='login')
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        return redirect('home')
    context={
    }
    return render(request ,'site1/delete.html',context)

@login_required(login_url='loginn')
def upload_documents(request,pk):
    stagiaire = Stagiaire.objects.get(id=pk)
    if request.method == 'POST':
        form = MultiDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # Save each document if it exists in the form
            if form.cleaned_data['cv']:
                Document.objects.create(stagiaire=stagiaire, typeDocumment='CV', document=form.cleaned_data['cv'])
            if form.cleaned_data['convention']:
                Document.objects.create(stagiaire=stagiaire, typeDocumment='Convocation', document=form.cleaned_data['convention'])
            if form.cleaned_data['assurance']:
                Document.objects.create(stagiaire=stagiaire, typeDocumment='Assurece', document=form.cleaned_data['assurance'])
            if form.cleaned_data['rapport']:
                Document.objects.create(stagiaire=stagiaire, typeDocumment='Rapport', document=form.cleaned_data['rapport'])
            if form.cleaned_data['lettre_motivation']:
                Document.objects.create(stagiaire=stagiaire, typeDocumment='LettreMotivation', document=form.cleaned_data['lettre_motivation'])
            messages.success(request, 'Documents uploaded successfully!')
            return redirect('home')
    else:
        form = MultiDocumentForm()
    documents = Document.objects.filter(stagiaire=stagiaire)
    context = {
        'form': form,
        'stagiaire': stagiaire,
    }
    return render(request, 'site1/uplo.html', context)

@login_required(login_url='loginn')
def stagiere(request,pk):
    
    stagia = get_object_or_404(Stagiaire, id=pk)
    cat1 = Stage.objects.filter(stagiaire=stagia)
    documents = Document.objects.filter(stagiaire=stagia)
    context = {
        'documents': documents,
        'stagiare': stagia,
        'cat1': cat1,
    }
    return render(request,'site1/etudiant.html',context)




@login_required(login_url='login')
@allowedUsers(allowedUsers=['encadrent','admin'])
def edit_user(request):
    user =request.user
    form = Creatform(instance=user)
    if request.method == 'POST':
        form = Creatform(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'site1/edittt.html', context)