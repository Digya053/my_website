"""Defines URL patterns for website."""

from django.urls import path

from . import views

urlpatterns = [
	path('', views.home),
	path('home/', views.home, name='home'),
	path('articles/technical', views.technical, name='technical'),
	path('articles/nontechnical', views.nontechnical, name='nontechnical'),
	path('contact/', views.contact, name='contact'),
]
