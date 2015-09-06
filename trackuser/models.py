from django.db import models
from django.utils import timezone

class Create(models.Model):
	email = models.EmailField(unique=True,max_length=100)
	username = models.CharField(unique=True, max_length=100)
	password = models.CharField(max_length=100)
	
	
	def __str__(self):
		return self.username

class Profile(models.Model):
	user = models.OneToOneField(Create,unique = True)
	full_name= models.CharField(max_length=100,null=True,blank=True)
	address = models.CharField(max_length=1000,null=True,blank=True)
	phone_number = models.CharField(max_length=13,null=True,blank=True)

	def __str__(self):
		return self.user

class Post(models.Model):
	author = models.ForeignKey()
	title = models.CharField(max_length=200)
	text=models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title
