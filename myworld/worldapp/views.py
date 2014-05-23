from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	title = 'This is Tung\'s world'
	context = {
		'page_title': title,
	}
	return render(request, 'worldapp/index.html', context)
# Create your views here.
