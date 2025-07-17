from django.shortcuts import render
from .models import About

# Create your views here.

def about_me(request):
    """
    Display an About Me page using content from the database.
    """
    # Get all About objects, order by updated_on in reverse order, and return the first (most recent)
    about = About.objects.all().order_by('-updated_on').first()
    
    return render(
        request,
        "about/about.html",
        {"about": about},
    )
