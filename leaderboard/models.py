from django.db import models
from django.contrib import admin
from django.db.models.deletion import CASCADE
from .choices import Game_Choices, Team_Game_Choices
from decimal import Decimal
from django.db.models import F, Sum


class Customer(models.Model):
    nickname = models.CharField(max_length=30, verbose_name="Nickname")
    totalScore = models.IntegerField(
        default=0, verbose_name="Totaalscore", editable=False
    )
    totalScoreFifa = models.IntegerField(
        default=0, verbose_name="totaalScore Fifa", editable=False
    )
    totalScoreMarioKart = models.IntegerField(
        default=0, verbose_name="totaalScore Mario Kart", editable=False
    )
    totalScoreRocketLeague = models.IntegerField(
        default=0, verbose_name="totaalScore Rocket League", editable=False
    )
    totalScoreVersus = models.IntegerField(
        default=0, verbose_name="totaalScore Versus", editable=False
    )

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = "Klant"
        verbose_name_plural = "Klanten"


class Matche(models.Model):
    game_id = models.CharField(
        max_length=30,
        blank=False,
        choices=Game_Choices,
        verbose_name="Naam van de game",
    )
    winnaar = models.ForeignKey(
        Customer,
        on_delete=CASCADE,
        blank=False,
        related_name="winnaar",
        verbose_name="Winnaar",
    )
    verliezer = models.ForeignKey(
        Customer,
        on_delete=CASCADE,
        blank=False,
        related_name="verliezer",
        verbose_name="Verliezer",
    )

    def __str__(self):
        template = "{0.winnaar} VS {0.verliezer} || {0.game_id}"
        return template.format(self)

    class Meta:
        verbose_name = "1v1 Wedstrijd"
        verbose_name_plural = "1v1 Wedstrijden"


class Teams(models.Model):
    teamName = models.CharField(
        max_length=30,
        verbose_name="Team naam",
        default="",
    )
    totalTeamScoreVersus = models.IntegerField(
        default=0, verbose_name="totaalScore Versus", editable=False
    )
    totalTeamScoreDeadAhead = models.IntegerField(
        default=0, verbose_name="totaalScore Dead Ahead", editable=False
    )
    totalTeamScoreCyberShock = models.IntegerField(
        default=0, verbose_name="totaalScore Cyber Shock", editable=False
    )
    totalTeamScoreArrowSong = models.IntegerField(
        default=0, verbose_name="totaalScore Arrow Song", editable=False
    )
    totalTeamScoreQuantumArena = models.IntegerField(
        default=0, verbose_name="totaalScore Quantum Arena", editable=False
    )
    totalTeamScoreQub3zShooter = models.IntegerField(
        default=0, verbose_name="totaalScore Qub3z Shooter", editable=False
    )
    player1 = models.ForeignKey(
        Customer,
        on_delete=CASCADE,
        blank=False,
        related_name="player1",
        verbose_name="player1",
    )
    player2 = models.ForeignKey(
        Customer,
        on_delete=CASCADE,
        blank=False,
        related_name="player2",
        verbose_name="Player2",
    )
    player3 = models.ForeignKey(
        Customer,
        on_delete=CASCADE,
        null=True,
        blank=True,
        related_name="player3",
        verbose_name="Player3",
    )
    player4 = models.ForeignKey(
        Customer,
        on_delete=CASCADE,
        null=True,
        blank=True,
        related_name="player4",
        verbose_name="Player4",
    )
    totalScoreVersus = models.IntegerField(
        default=0, verbose_name="totaalScore Versus", editable=False
    )

    def __str__(self):
        return self.teamName

    class Meta:
        verbose_name = "Teams"
        verbose_name_plural = "Teams"


class TeamWedstrijden(models.Model):
    game_id = models.CharField(
        max_length=30,
        blank=False,
        choices=Team_Game_Choices,
        verbose_name="Naam van de game",
    )
    team = models.ForeignKey(
        Teams,
        on_delete=CASCADE,
        blank=False,
        related_name="team",
        verbose_name="Team",
    )
    score = models.IntegerField(default=0, verbose_name="Totale score")

    def __str__(self):
        template = "{0.team} || {0.score}"
        return template.format(self)

    class Meta:
        verbose_name = "Team Wedstrijden"
        verbose_name_plural = "Team Wedstrijden"
