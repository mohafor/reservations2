from django.contrib import admin
from .models import Show
from .models import Artist
from .models import Role
from .models import Representation
from .models import Type
from .models import User

# Register your models here.
admin.site.register(Show)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'title', 'description', 'poster_url', 'location_id', 'bookable', 'price', 'created_at')

admin.site.register(Artist)
class UserAdmin(admin.ModelAdmin):
    list_display =('firstname', 'lastname')

admin.site.register(Role)
class UserAdmin(admin.ModelAdmin):
    list_display =('role')

admin.site.register(Type)
class UserAdmin(admin.ModelAdmin):
    list_display =('type')

admin.site.register(Representation)
class UserAdmin(admin.ModelAdmin):
    list_display =('show', 'schedule', 'location')

admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display =('login', 'password', 'firstname', 'lastname', 'email', 'langue')