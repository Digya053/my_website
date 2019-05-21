from django.shortcuts import render

def home(request):
	return render(request, 'webapp/home.html')

def technical(request):
	return render(request, 'webapp/technical.html')

def nontechnical(request):
	return render(request, 'webapp/non-technical.html')

def contact(request):
	return render(request, 'webapp/contact.html')
