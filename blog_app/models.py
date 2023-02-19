from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=20,null=False)
    last_name=models.CharField(max_length=20,null=False)
    location=models.CharField(max_length=20,null=False)  
    hobby=models.CharField(max_length=20,null=False) 
    email_id=models.CharField(max_length=20,null=False) 
    phone_num=models.IntegerField(default=0)
    def __str__(self):
        return "%s %s "%(self.first_name, self.location)

class Category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Blog(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=35)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)    
    def __str__(self):
        return self.title
        