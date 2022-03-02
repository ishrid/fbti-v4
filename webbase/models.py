from django.db import models

class AlbiDOro(models.Model):
 
    nome = models.CharField(max_length=255)
    attivo = models.BooleanField(default=True)
    img = models.ImageField(upload_to='albiDoro/img', blank=True, null=True) 
    pdf = models.FileField(upload_to='albiDoro/pdf')  

    def __str__(self):
        return self.nome 


class Regolamenti(models.Model):
 
    nome = models.CharField(max_length=255)
    attivo = models.BooleanField(default=True)
    anno= models.IntegerField(blank=True, null=True)
    pdf = models.FileField(upload_to='regolamenti')  

    def __str__(self):
        return self.nome 

class Classifiche(models.Model):
 
    nome = models.CharField(max_length=255)
    attivo = models.BooleanField(default=True)
    anno= models.IntegerField(blank=True, null=True)
    pdf = models.FileField(upload_to='classifiche')  

    def __str__(self):
        return self.nome 


class Categorie(models.Model):
 
    nome = models.CharField(max_length=255)
    attivo = models.BooleanField(default=True)
    anno= models.IntegerField(blank=True, null=True)
    pdf = models.FileField(upload_to='categorie')  

    def __str__(self):
        return self.nome 




class Calendari(models.Model):
 
    nome = models.CharField(max_length=255)
    attivo = models.BooleanField(default=True)
    anno= models.IntegerField(blank=True, null=True)
    pdf = models.FileField(upload_to='calendari')  

    def __str__(self):
        return self.nome 