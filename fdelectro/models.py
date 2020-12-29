from django.db import models


class register(models.Model):

	idf = models.AutoField(primary_key=True)
	firstName=models.CharField(max_length=200)
	lastName=models.CharField(max_length=200)
	Identifiant=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	grade=models.CharField(max_length=200)
	def __str__(self):
		return self.firstName
	
class signin(models.Model):

	Identifiant=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
