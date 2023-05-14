from django.contrib import admin
from .models import Show
from .models import Location
from .models import Locality
from .models import Artist
from .models import Type
from .models import ArtistType
from .models import ArtistTypeShow

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

admin.site.register(Artist)
admin.site.register(Type)
admin.site.register(ArtistType)
admin.site.register(ArtistTypeShow)