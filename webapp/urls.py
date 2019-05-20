"""Defines URL patterns for website."""

from django.urls import path

from . import views

urlpatterns = [
	# Home page
	path('', views.home),
	path('home/', views.home, name='home'),
	#url('/articles', views.articles, name='articles'),
	#path('/contact', views.contact, name='contact'),
	
]
