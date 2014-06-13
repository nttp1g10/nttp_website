from django.conf.urls import patterns, url
from worldapp import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'recipe/', views.recipe),
	url(r'profile/', views.profile),
	url(r'admin/', views.admin),
)