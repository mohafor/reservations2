from django.db import models
from .user import User

# Create your models here.
class Role(models.Model):
	role = models.CharField(max_length=30)
	user = models.ManyToManyField(User, through='RoleUser')
	
	class Meta:
		db_table = "roles"
