from django.contrib import admin
from django.urls import path

from list_jobs.views import LoginView, RegisterView,HomeView,JobListView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('joblist/', JobListView.as_view(), name='joblist'),
    path('', HomeView.as_view(), name='home')
]