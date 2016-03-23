from django.db import models
from django.contrib.auth.models import User

class userprofile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	idno = models.CharField(max_length=20)
