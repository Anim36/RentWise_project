from django.contrib import admin
from .models import Booking, Category, Location, Property  # Remove 'Review' from imports

# Register your models here.
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Property)
admin.site.register(Booking)