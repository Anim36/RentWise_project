from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from properties.models import Property


class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]

    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=True)  # Auto-approve for now

    class Meta:
        unique_together = ['property', 'user']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.property.title} - {self.rating} stars"