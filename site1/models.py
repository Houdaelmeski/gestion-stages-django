from django.db import models

# Create your models here.
from django.db.models import Count
#user import...
from django.contrib.auth.models import User


    
class Encadrent(models.Model):

    user=models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    prenom = models.CharField(max_length=200, null=True)
    nom = models.CharField(max_length=200, null=True)
    email=models.EmailField(max_length=200, null=True)
    post = models.CharField(max_length=500, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='profile/',default="png.png")
    def __str__(self):
        return self.nom
    
    @property
    def num_stages(self):
        return self.stage_set.count()
    
    
class Stagiaire(models.Model):
    user=models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    prenom = models.CharField(max_length=200, null=True)
    nom = models.CharField(max_length=200, null=True)
    ecole = models.CharField(max_length=200, null=True)
    email=models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    age=models.CharField(max_length=50, null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    niv=models.CharField(max_length=200)
    image = models.ImageField(upload_to='profile/',default="png.png")
    
    def __str__(self):
        return self.nom
    

class Stage(models.Model):
    TYPE ={
        ('Observation', 'Observation'),
        ('Application', 'Application'),
        ('Embouchement','Embouchement'),
    }
    status ={
        ('Encours', 'Encours'),
        ('PasEncore', 'PasEncore'),
        ('Fin','Fin'),
    }

    # <p>Email : <a href="mailto:jean.dupont@example.com">jean.dupont@example.com</a></p>
    nom= models.CharField(max_length=50,blank=True, null=True)
    encadrent = models.ForeignKey(Encadrent,null =True,on_delete=models.SET_NULL)
    note = models.FloatField( blank=True, null=True)
    commentaire=models.TextField(blank=True, null=True)
    dateDebut=models.DateField(blank=True, null=True)
    dateFin=models.DateField(blank=True, null=True)
    Suject = models.TextField(blank=True, null=True)
    Source = models.TextField(blank=True, null=True)
    statusStage=models.CharField(max_length=50, choices=status , default='PasEncore')
    type = models.CharField(max_length=50, choices=TYPE , default='Observation')
    stagiaire = models.ForeignKey(Stagiaire,null =True,on_delete=models.SET_NULL)

    

    

class Document(models.Model):

    TYPE ={
        ('LettreMotivation', 'LettreMotivation'),
        ('CV', 'CV'),
        ('Assurece','Assurece'),
        ('Convocation','Convocation'),
        ('Rapport','Rapport'),
    }
    stagiaire = models.ForeignKey(Stagiaire,null =True,on_delete=models.SET_NULL)
    typeDocumment = models.CharField(max_length=50, choices=TYPE , default='Observation')
    document = models.FileField(upload_to='document/',blank=True, null=True)    
    def __str__(self):
        return self.typeDocumment
