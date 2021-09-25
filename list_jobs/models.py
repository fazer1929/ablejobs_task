from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):    
    email = models.EmailField(('email address'), unique=True) 


class Job(models.Model):
    job_roles=(
        ('BDE',"Buisness Development Executive"),
        ('CSV',"Customer Support Voice"),
        ('CSN',"Customer Support Non-Voice"),
        ('IS',"Inside Sales"),
        ('FS',"Feild Sales"),
        ('CW',"Content Writing"),
        ('DM',"Digital Marketing"),
        ('OT',"Others"),
    )
    job_role = models.CharField(max_length=30,choices=job_roles)
    job_description = models.TextField()
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=12)
    owner = models.ForeignKey(to=CustomUser,on_delete=models.CASCADE)
