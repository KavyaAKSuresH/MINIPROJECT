from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')

def register_complaint(request):
    return render(request, 'register.html')

def track_complaint(request):
    return render(request, 'track.html')

def view_complaint(request):
    return render(request, 'viewcomplaint.html')



# Dashboard views
def facultyhome(request):
    return render(request, 'facultydash.html')
def notifications(request):
    return render(request, 'notifications.html')

def new_complaints(request):
    return render(request, 'new_complaints.html')

def pending_complaints(request):
    return render(request, 'pending_complaints.html')

def resolved_complaints(request):
    return render(request, 'resolved_complaints.html')

def profile(request):
    return render(request, 'profile.html')

def logout_view(request):
    return HttpResponse("You have been logged out.")

