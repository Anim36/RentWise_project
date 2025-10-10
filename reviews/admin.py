from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'property', 'rating', 'is_approved', 'created_at']
    list_filter = ['rating', 'is_approved', 'created_at']
    search_fields = ['user__username', 'property__title', 'comment']
    list_editable = ['is_approved']


from django.contrib import admin

# Register your models here.
