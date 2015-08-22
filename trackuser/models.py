from django.db import models

class createuser(models.Model):
	name = models.CharField(max_length=100)
	place = models.CharField(max_length=100)


