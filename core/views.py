from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Event
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required
def my_rsvps(request):
    # Get all events that the logged-in user has RSVP'd to
    events = request.user.events_participated.all()
    return render(request, 'core/my_rsvps.html', {'events': events})

@login_required
def rsvp_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user in event.participants.all():
        event.participants.remove(request.user)
    else:
        event.participants.add(request.user)
    # Redirect to "My RSVPs" page after RSVP action
    return redirect('my_rsvps')


def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def events(request):
    return render(request, 'core/events.html')

def join(request):
    return render(request, 'core/join.html')

@login_required
def events_list(request):
    events = Event.objects.all().order_by('date')  # Order events by date
    return render(request, 'core/events_list.html', {'events': events})
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})
    
@login_required
def rsvp_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user in event.participants.all():
        event.participants.remove(request.user)
    else:
        event.participants.add(request.user)
    return HttpResponseRedirect(reverse('events'))  # Redirect back to the events list
    
@login_required
def rsvp_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user in event.participants.all():
        event.participants.remove(request.user)
    else:
        event.participants.add(request.user)
    # Redirect to "My RSVPs" page after RSVP action
    return redirect('my_rsvps')
