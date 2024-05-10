from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField("Username" ,max_length=30)
    email = models.EmailField("Email" ,max_length=30)
    password = models.CharField("Password" ,max_length=30)

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = "hambal"
        verbose_name_plural = "hambalner"   

class Tasks(models.Model):
    task = models.CharField("Task" , max_length=200)
    status = models.BooleanField("Status" , default=False)

