from django.db import models
from django.db.models.deletion import CASCADE
from .choices import Game_Choices
from decimal import Decimal
from django.db.models import F, Sum



class Customer(models.Model):
    nickname = models.CharField(max_length=30, verbose_name="Nickname")
    totalScore = models.IntegerField(default=0, verbose_name="Totaalscore")
    totalScoreFifa = models.IntegerField(default=0, verbose_name="totaalScore Fifa")
    totalScoreMarioKart = models.IntegerField(default=0, verbose_name="totaalScore Mario Kart")
    totalScoreRocketLeague = models.IntegerField(default=0, verbose_name="totaalScore Rocket League")


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
        verbose_name = "Wedstrijd"
        verbose_name_plural = "Wedstrijden"
