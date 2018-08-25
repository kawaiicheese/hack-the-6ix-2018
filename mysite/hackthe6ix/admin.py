from django.contrib import admin

from .models import Person, Listings
# Register your models here.

admin.site.register(Person)
admin.site.register(Listings)