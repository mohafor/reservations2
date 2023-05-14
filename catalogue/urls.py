"""reservations.catalogue URL Configuration
"""
from django.urls import path

from . import views

app_name='catalogue'

urlpatterns = [
    path('artist/', views.artist.index, name='artist_index'),
    path('artist/create/', views.artist.create, name='artist_create'),
    path('artist/<int:artist_id>', views.artist.show, name='artist_show'),
    path('artist/<int:artist_id>/edit/', views.artist.edit, name='artist_edit'),
    path('artist/<int:artist_id>/delete', views.artist.delete, name='artist_delete'),
    path('type/', views.type.index, name='type_index'),
    path('type/<int:type_id>', views.type.show, name='type_show'),
    path('locality/', views.locality.index, name='locality_index'),
    path('locality/<int:locality_id>', views.locality.show, name='locality_show'),
    path('role/', views.role.index, name='role_index'),
    path('role/<int:role_id>', views.role.show, name='role_show'),
    path('location/', views.location.index, name='location_index'),
    path('location/<int:location_id>', views.location.show, name='location_show'),
    path('show/', views.show_detail.index, name='show_index'),
    path('show/<int:show_id>', views.show_detail.show, name='show_show'),
    path('representation/', views.representation.index, name='representation_index'),
    path('representation/<int:representation_id>', views.representation.show, name='representation_show'),
]