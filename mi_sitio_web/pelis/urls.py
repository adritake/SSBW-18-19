from django.urls import path

from . import views

urlpatterns = [
	path('buscar/', views.find),
	path('mostrarpelis/', views.mostrar_pelis),
	path('infopeli/<id>', views.info_peli),
	path('borrapeli/<id>', views.borra_peli),
	path('aniadirpeli/',views.aniadir_peli),
	path('aniadepeli/<titulo>/<sinopsis>/<director>/<actor>/<genero>/<year>',views.aniade_peli),
	path('edicionpeli/<id>', views.edicion_peli),
	path('editapeli/<id>/<sinopsis>/<director>/<genero>/<year>', views.edita_peli),
	path('like', views.like),
	path('dislike', views.dislike),
	path('api_pelis',    views.api_pelis),  # GET lista todas, POST añade
	path('api_peli/<id>', views.api_peli),  # GET lista una,   PUT modifica, DELETE borra
	]
