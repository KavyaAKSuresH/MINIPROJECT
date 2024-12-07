from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def register_complaint(request):
    return render(request, 'register.html')

def track_complaint(request):
    return render(request, 'track.html')


