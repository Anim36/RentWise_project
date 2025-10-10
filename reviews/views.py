from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from properties.models import Property
from .models import Review
from .forms import ReviewForm


@login_required
def add_review(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    existing_review = Review.objects.filter(property=property, user=request.user).first()

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=existing_review)
        if form.is_valid():
            review = form.save(commit=False)
            review.property = property
            review.user = request.user
            review.save()
            messages.success(request, 'Thank you for your review!')
            return redirect('property_details', id=property.id)
    else:
        form = ReviewForm(instance=existing_review)

    return render(request, 'add_review.html', {
        'form': form,
        'property': property,
        'existing_review': existing_review
    })