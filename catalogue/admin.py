from django.contrib import admin
from .models import Show
from .models import Location
from .models import Locality
from .models import Artist
from .models import Type
from .models import ArtistType
from .models import ArtistTypeShow
from .models import Representation
from .models import RepresentationUser
from .models import Role
from .models import RoleUser
from .models import User

# Register your models here.
@admin.register(Show)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'title', 'description', 'poster_url', 'location_id', 'bookable', 'price', 'created_at')

@admin.register(Location)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'designation', 'address', 'website', 'phone', 'locality_id')


@admin.register(Locality)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'postal_code', 'locality')

@admin.register(Representation)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'schedule', 'location_id', 'show_id')

@admin.register(RepresentationUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'places', 'representation_id', 'user_id')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'role')

@admin.register(RoleUser)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'user')

admin.site.register(Artist)
admin.site.register(Type)
admin.site.register(ArtistType)
admin.site.register(ArtistTypeShow)
admin.site.register(User)