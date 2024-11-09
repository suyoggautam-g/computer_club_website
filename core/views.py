from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def events(request):
    return render(request, 'core/events.html')

def join(request):
    return render(request, 'core/join.html')

