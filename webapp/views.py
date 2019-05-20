from django.shortcuts import render

def home(request):
	return render(request, 'webapp/home.html')

def articles(request):
	return render(request, 'webapp/articles.html')
