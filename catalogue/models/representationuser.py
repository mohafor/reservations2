from django.db import models
from .representation import Representation
from .user import User

class RepresentationUser(models.Model):
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    places = models.IntegerField()

    class Meta:
        db_table = 'representation_user'