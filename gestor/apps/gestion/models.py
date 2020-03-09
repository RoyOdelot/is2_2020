from django.db import models

# Create your models here.

class Usuario(models.Model):
	usuario_id = models.IntegerField(primary_key=True)
	nom_cuenta = models.CharField(max_length=50)
	usuario_pass = models.CharField(max_length=20)
		
