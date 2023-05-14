from django.db import models

# Create your models here.
class Role(models.Model):
	role = models.CharField(max_length=30)
	
	class Meta:
		db_table = "roles"
