from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('events/', views.events_list, name='events'),
    path('join/', views.join, name='join'),
    path('register/', views.register, name='register'),  # Registration page
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),  # Login page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout page
    path('events/rsvp/<int:event_id>/', views.rsvp_event, name='rsvp_event'),
    path('my-rsvps/', views.my_rsvps, name='my_rsvps'),


]
