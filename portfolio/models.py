from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    subject =models.TextField()
    message =models.TextField()

    def __str__(self):
        return self.name



class Blog(models.Model):
    title =models.CharField(max_length=60)
    description=models.TextField()  
    authname=models.CharField(max_length=15)
    img=models.ImageField(upload_to='blog',blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
     return self.title