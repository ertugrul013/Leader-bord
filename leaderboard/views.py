from django.db.models.query import InstanceCheckMeta
from django.http import request
from django.shortcuts import render, redirect
from .models import Customer, Matche, Teams, TeamWedstrijden
from .choices import Game_Choices
from django.db.models import IntegerField



def fifa_score(request):
    TotalScore = Customer.objects.all().order_by("-totalScoreFifa")[:10]
    return render(request, "fifaScore.html", {"TotalScore": TotalScore})

def versus_score(request):
    TotalScore = Customer.objects.all().order_by("-totalScoreVersus")[:10]
    return render(request, "versusScore.html", {"TotalScore": TotalScore})

def versusTeams_score(request):
    TotalScore = Teams.objects.all().order_by("-totalTeamScoreVersus")[:10]
    return render(request, "versusTeamsScore.html", {"TotalScore": TotalScore})

def qub3zshooterteams_score(request):
    TotalScore = Teams.objects.all().order_by("-totalTeamScoreQub3zShooter")[:10]
    return render(request, "qub3zShooterTeamsScore.html", {"TotalScore": TotalScore})

def marioKart_score(request):
    TotalScore = Customer.objects.all().order_by("-totalScoreMarioKart")[:10]
    return render(request, "marioKartScore.html", {"TotalScore": TotalScore})

def rocketLeague_score(request):
    TotalScore = Customer.objects.all().order_by("-totalScoreRocketLeague")[:10]
    return render(request, "rocketLeagueScore.html", {"TotalScore": TotalScore})

def totalScores(request):
    TotalScore = Customer.objects.all().order_by("-totalScore")[:10]
    return render(request, "totalScores.html", {"TotalScore": TotalScore})

def deadAhead_score(request):
    TotalScore = Teams.objects.all().order_by("-totalTeamScoreDeadAhead")[:10]
    return render(request, "deadAheadScore.html", {"TotalScore": TotalScore})

def cyberShock_score(request):
    TotalScore = Teams.objects.all().order_by("-totalTeamScoreCyberShock")[:10]
    return render(request, "cyberShockScore.html", {"TotalScore": TotalScore})

def arrowSong_score(request):
    TotalScore = Teams.objects.all().order_by("-totalTeamScoreArrowSong")[:10]
    return render(request, "ArrowSongScore.html", {"TotalScore": TotalScore})

def quantumArena_score(request):
    TotalScore = Teams.objects.all().order_by("-totalTeamScoreQuantumArena")[:10]
    return render(request, "quantumArenaScore.html", {"TotalScore": TotalScore})
