"""Defines URL patterns for website."""

from django.urls import path

from . import views

urlpatterns = [
	path('', views.home),
	path('home/', views.home, name='home'),
	path('articles/technical', views.technical, name='technical'),
	path('articles/non-technical', views.nontechnical, name='non-technical'),
	path('contact/', views.contact, name='contact'),
]
