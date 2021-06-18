from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()

    def __str__(self):
        return f"{self.title}"
        
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    address=models.CharField(max_length=1000)
    msg=models.CharField(max_length=400)

    def __str__(self):
        return f"massage from {self.name}"