from django.db.models.query import InstanceCheckMeta
from django.http import request
from django.shortcuts import render, redirect
from .models import Customer
from .models import Matche
from .choices import Game_Choices
from django.db.models import Sum



def fifa_score(request):
    customer = Customer.objects.all().order_by("-totalScore")[:10]
    return render(request, "fifaScore.html", {"customer": customer})


def marioKart_score(request):
    customer = Customer.objects.all().order_by("-totalScore")[:10]
    return render(request, "marioKartScore.html", {"customer": customer})

def rocketLeague_score(request):
    customer = Customer.objects.all().order_by("-totalScore")[:10]
    return render(request, "rocketLeagueScore.html", {"customer": customer})

def totalScores(request):
    customer = Customer.objects.all().order_by("-totalScore")[:10]
    return render(request, "totalScores.html", {"customer": customer})
