from django.db import models


#Create your models here.
class User(models.Model):
    login = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=225)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.EmailField('Email Address', null=True)
    langue = models.CharField(max_length=2)
    
class  Meta:
	db_table = 'users'

