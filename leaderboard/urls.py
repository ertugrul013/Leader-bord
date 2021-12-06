from django.urls import path
from .views import (
    fifa_score,
    totalScores,
    marioKart_score,
    rocketLeague_score,
    versus_score,
    versusTeams_score,
    qub3zshooterteams_score,
    deadAhead_score,
    cyberShock_score,
    arrowSong_score,
    quantumArena_score,    
)


urlpatterns = [
    path("", totalScores, name="totalScores"),
    path("fifa", fifa_score, name="fifa_score"),
    path("versus", versus_score, name="versus_score"),
    path("versusteams", versusTeams_score, name="versusTeams_score"),
    path("mariokart", marioKart_score, name="marioKart_score"),
    path("rocketleague", rocketLeague_score, name="rocketLeague_score"),
    path("qub3zshooterteamsscore", qub3zshooterteams_score, name="qub3zshooterteams_score"),
    path("deadahead", deadAhead_score, name="deadahead_score"),
    path("cybershock", cyberShock_score, name="cybershock_score"),
    path("arrowsong", arrowSong_score, name="arrowsong_score"),
    path("quantumarena", quantumArena_score, name="quantumarena_score"),

]
