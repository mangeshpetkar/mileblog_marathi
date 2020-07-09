from django.db import models

# Create your models here.

class Link(models.Model):
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    y_link= models.URLField()
    i_link= models.URLField()   


class Feedback(models.Model):
    username= models.CharField(max_length=50)
    useremail= models.EmailField()
    subject= models.CharField(max_length=50)
    message= models.CharField(max_length=200)       

class Articles(models.Model):
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics') 
    description= models.TextField()
   
    
  