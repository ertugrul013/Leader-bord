from django.urls import path
from .views import fifa_score, totalScores, marioKart_score, rocketLeague_score


urlpatterns = [
    path("", totalScores, name="totalScores"),
    path("fifa", fifa_score, name="fifa_score"),
    path("mariokart", marioKart_score, name="marioKart_score"),
    path("rocketleague", rocketLeague_score, name="rocketLeague_score"),
]
