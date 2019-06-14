from django.urls import path

from . import views

urlpatterns = [
	path('actor/<actor>', views.find_actor), # <lista> = Lista separada por "+"
	]
