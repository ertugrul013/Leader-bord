from django.db.models.query import InstanceCheckMeta
from django.http import request
from django.shortcuts import render, redirect
from .models import Customer
from .models import Matche
from .choices import Game_Choices
from django.db.models import IntegerField, F, Sum
from django.db.models import Count


def fifa_score(request):
    TotalScore = Customer.objects.all().order_by("-totalScoreFifa")[:10]
    return render(request, "fifaScore.html", {"TotalScore": TotalScore})

def marioKart_score(request):
    TotalScore = Customer.objects.all().order_by("-totalScoreMarioKart")[:10]
    return render(request, "marioKartScore.html", {"TotalScore": TotalScore})


def rocketLeague_score(request):
    TotalScore = Customer.objects.all().order_by("-totalScoreRocketLeague")[:10]
    return render(request, "rocketLeagueScore.html", {"TotalScore": TotalScore})


def totalScores(request):
    TotalScore = Customer.objects.all().order_by("-totalScore")[:10]
    return render(request, "totalScores.html", {"TotalScore": TotalScore})
