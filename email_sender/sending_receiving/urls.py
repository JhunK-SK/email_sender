from django.urls import path
from . import views

urlpatterns = [
    # Home Page.
    path('', views.index, name='home'),
    
    # Sending to one person.
    path('send_one/', views.send_one, name='send_one'),
    
    # Receiving message from users.
    path('receiving/', views.receiving, name='receiving'),
    
    # Sending a message with a uploaded file.
    path('send_file/', views.send_file, name='send_file'),
]