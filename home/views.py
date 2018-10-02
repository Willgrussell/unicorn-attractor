from django.shortcuts import render

# Create your views here.
def index(request):
    """A view that displays an index page"""
    return render(request, "index.html")
    
def contact(request):
    """A view that displays a contact us page"""
    return render(request, "contact.html")
    
def about(request):
    """A view that displays an about us page"""
    return render(request, "about.html")
    
def promotion(request):
    """A view that will display any promotion i choose to display"""
    return render(request, "promotions.html")