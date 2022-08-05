from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')