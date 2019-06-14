from django.shortcuts import render

from django.shortcuts import HttpResponse

from .models import Pelis

from django.http import JsonResponse

# import the logging library
import logging

import random

from .serializers import PelisSerializer


# Get an instance of a logger
logger = logging.getLogger(__name__)



def find(request):

    return render(request,'buscador.html')


def mostrar_pelis(request):

    nombre = request.GET.get('actor', None)
    genero = request.GET.get('genero', None)

    pelis = []

    if nombre != None:
        for peli in Pelis.objects(actors = nombre):
            pelis.append(peli)


        context = {
            'actor' : nombre,
            'pelis' : pelis,
        }

        return render(request, 'mostrarpelis.html', context)

    if genero != None:
        for peli in Pelis.objects(genres = genero):
            pelis.append(peli)


        context = {
            'genero' : genero,
            'pelis' : pelis,
        }

        return render(request, 'mostrarpelis.html', context)



def info_peli(request, id):

    peli = Pelis.objects.get(id = id)

    context = {
        'id' : id,
        'peli': peli,
    }

    logger.info('Mostrada información de la película con id = {}'.format(id))

    return render(request, 'infopeli.html', context)


def edicion_peli(request, id):

    peli = Pelis.objects.get(id = id)

    context = {
        'id' : id,
        'peli': peli,
    }


    return render(request, 'editarpeli.html', context)


def edita_peli(request, id, sinopsis, director, genero, year):


    peli = Pelis.objects.get(id = id);
    peli.plot = sinopsis;
    peli.director = director;
    peli.genres = genero.split(',');
    peli.year = year;
    peli.save();

    return JsonResponse({'status':'OK'})

def borra_peli(request, id):

    Pelis.objects.get(id=id).delete()
    logger.info("Se ha borrado la película con id = {}".format(id))
    return JsonResponse({'status':'OK'})


def aniadir_peli(request):

    return render(request, 'aniadirpeli.html')

def aniade_peli(request, titulo, sinopsis, director, actor, genero, year):


    peli = Pelis(title=titulo,plot=sinopsis,director=director,actors=actor.split(','),genres=genero.split(','),year=year);
    peli.save();

    return JsonResponse({'status':'OK'})


def like(request):
    return JsonResponse({'number':random.randint(1,1001)})

def dislike(request):
    return JsonResponse({'number':random.randint(1,1001)})



from django.http import JsonResponse

# Listar todas, Añadir
def api_pelis(request):
	if request.method == 'GET':
		pelis = Pelis.objects.all()[:10]
		serializer = PelisSerializer(pelis, many=True)
		return JsonResponse(serializer.data, safe=False)

	if request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = PelisSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)

	logger.debug('Error')
	return JsonResponse(serializers.errors, status=400)


# Listar, Modificar, Borrar
def api_peli(request, id):
    try:
        peli = Pelis.objects().get(id=id)
    except:
        logger.debug('Peli no encontrada '+id)
        return HttpResponse(status=404)  # No encontrado

    if request.method == 'GET':
        serializer = PelisSerializer(peli)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PelisSerializer(data=data)

        peli.title = data.title
        peli.title       = data.title
        peli.year        = data.year
        peli.rated       = data.rated
        peli.runtime     = data.runtime
        peli.countries   = data.countries
        peli.genres      = data.genres
        peli.director    = data.director
        peli.writers     = data.writers
        peli.actors      = data.actors
        peli.plot        = data.plot
        peli.poster      = data.poster
        peli.imdb        = data.imdb
        peli.tomato      = data.tomato
        peli.metacritic  = data.metacritic
        peli.awards      = data.awards
        peli.type        = data.type

        peli.save()
        return JsonResponse(serializer.data, status=200)

    if request.method == 'DELETE':
        peli.delete()
        return HttpResponse(status=200)  # No encontrado
