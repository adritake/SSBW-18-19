from django.shortcuts import render

from django.shortcuts import HttpResponse

from .models import Pelis

import pymongo
from pymongo import MongoClient
import requests
import re

client = MongoClient('mongo',27017)
db = client.movies
pelis = db.pelis

def find_actor(request, actor):

    lista = pelis.find({'actors':actor})

    context = {
        'actor' : actor,
        'lista' : lista
    }

    return render(request,'main.html', context)
