from django.shortcuts import render
from .models import About

# Create your views here.

def about_me(request):
    """
    Display an About Me page using content from the database.
    """
    # Get the first (and ideally only) About instance
    about = About.objects.first()
    
    return render(
        request,
        "about/about.html",
        {"about": about},
    )
