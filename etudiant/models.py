from django.db import models

# Create your models here.

class LoginInfo(models.Model):
    username=models.CharField(("username"),max_length=50, unique=True)
    password=models.CharField(("password"),max_length=50)
    email=models.EmailField(("email"),max_length=50)
    
    def __str__(self):
        return str(self.username)