from django.forms import ModelForm
from django import forms
from .models import *
#autontification...
from django.contrib.auth.forms import *
from django.contrib.auth.models import User

class EncadrentCreatForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    prenom = forms.CharField(max_length=30, required=True, help_text='Required')
    nom = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, required=True, help_text='Required')
    post = forms.CharField(max_length=50, required=True, help_text='Required')
    phone = forms.CharField(max_length=15, required=True, help_text='Required')
    image = forms.ImageField(required=False)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('prenom')
        user.last_name = self.cleaned_data.get('nom')
        if commit:
            user.save()
            encadrent = Encadrent(user=user,
                                  prenom=self.cleaned_data.get('prenom'),
                                  nom=self.cleaned_data.get('nom'),
                                  email=self.cleaned_data.get('email'),
                                  post=self.cleaned_data.get('post'),
                                  phone=self.cleaned_data.get('phone'),
                                  image=self.cleaned_data.get('image'),
                                  )
            encadrent.save()

class Creatform(UserCreationForm):
    class Meta:
        model = User
        fields=['username','password1', 'password2']


class EncadrentForm(ModelForm):
    class Meta:
        model=Encadrent
        fields=['prenom','nom', 'email','post','phone', 'image']


class StageForm(ModelForm):
    class Meta:
        model=Stage
        fields="__all__"


class EncdForm(ModelForm):
    class Meta:
        model=Encadrent
        fields="__all__"


class StagiereCreatForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    prenom = forms.CharField(max_length=50, required=True, help_text='Required')
    nom = forms.CharField(max_length=50, required=True, help_text='Required')
    ecole = forms.CharField(max_length=50, required=True, help_text='Required')
    email=forms.EmailField(max_length=254, required=True, help_text='Required')
    phone = forms.CharField(max_length=15, required=True, help_text='Required')
    age=forms.CharField(max_length=30, required=True, help_text='Required')
    niv=forms.CharField(max_length=50, required=True, help_text='Required')


    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('prenom')
        user.last_name = self.cleaned_data.get('nom')
        if commit:
            user.save()
            stagiere = Stagiaire(user=user,
                                  prenom=self.cleaned_data.get('prenom'),
                                  nom=self.cleaned_data.get('nom'),
                                  email=self.cleaned_data.get('email'),
                                  ecole=self.cleaned_data.get('ecole'),
                                  niv=self.cleaned_data.get('niv'),
                                  age=self.cleaned_data.get('age'),
                                  phone=self.cleaned_data.get('phone'),
                                  )
            stagiere.save()

class MultiDocumentForm(forms.Form):
    cv = forms.FileField(required=False)
    convention = forms.FileField(required=False)
    assurance = forms.FileField(required=False)
    rapport = forms.FileField(required=False)
    lettre_motivation = forms.FileField(required=False)

class SearchForm(forms.Form):
    nom_stage = forms.CharField(required=False, max_length=255)
    encadrant = forms.CharField(required=False, max_length=255)
    stagiaire = forms.CharField(required=False, max_length=255)
    type_stage = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'Type de Stage'),
            ('Observation', 'Observation'),
            ('Application', 'Application'),
            ('Embouchement', 'Embouchement'),
        ]
    )

class EditStagiereForm(forms.Form):

    prenom = forms.CharField(max_length=50, required=False, help_text='Required')
    nom = forms.CharField(max_length=50, required=False, help_text='Required')
    ecole = forms.CharField(max_length=50, required=False, help_text='Required')
    email=forms.EmailField(max_length=254, required=False, help_text='Required')
    phone = forms.CharField(max_length=15, required=False, help_text='Required')
    age=forms.CharField(max_length=30, required=False, help_text='Required')
    niv=forms.CharField(max_length=50, required=False, help_text='Required')
    image=forms.ImageField(required=False)
    password=forms.CharField(max_length=30, required=False, help_text='Required')
    username=forms.CharField(max_length=30, required=False, help_text='Required')


    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('prenom')
        user.last_name = self.cleaned_data.get('nom')
        user.username = self.cleaned_data.get('username')
        user.password=self.cleaned_data.get('password')
        if commit:
            user.save()
            stagiere = Stagiaire(user=user,
                                  prenom=self.cleaned_data.get('prenom'),
                                  nom=self.cleaned_data.get('nom'),
                                  email=self.cleaned_data.get('email'),
                                  ecole=self.cleaned_data.get('ecole'),
                                  niv=self.cleaned_data.get('niv'),
                                  age=self.cleaned_data.get('age'),
                                  phone=self.cleaned_data.get('phone'),
                                  image=self.cleaned_data.get('image')
                                  )
            stagiere.save()

class imgstagiere(forms.ModelForm):
    class Meta:
        model = Stagiaire
        fields = ['image']

class imgstagiere(forms.ModelForm):
    class Meta:
        model = Encadrent
        fields = ['image']
