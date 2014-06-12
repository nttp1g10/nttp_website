from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	title = 'This is Tung\'s world'
	context = {
		'page_title': title,
	}
	return render(request, 'worldapp/index.html', context)
# Create your views here.

def recipe(request):
	return render(request, 'worldapp/recipe.html')

def profile(request):
	return render(request, 'worldapp/profile.html')

def admin(request):
	return render(request, 'worldapp/admin.html')