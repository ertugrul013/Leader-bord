from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Customer, Matche, TeamWedstrijden, Teams

"""A receiver function that's executed every time a post-save is sent from Customer

    A post-save signal is broadcasted when a model's save method completes successfully.

    Args that Django will pass to this post-save receiver:

    - sender
        The model class.
    - instances
        The actual instance being saved.
    - created
        A boolean; True if a new record was created.
    - raw
        A boolean; True if the model is saved exactly as presented (i.e. when loading
        a fixture). One should not query/modify other records in the database as the
        database might not be in a consistent state yet.
    - using
        The database alias being used.
    - update_fields
        The set of fields to update as passed to Model.save(), or None if update_fields
        wasn’t passed to save().
"""


@receiver(post_save, sender=Matche)
def updateTotalScore(sender, instance, created, **kwargs):
    if created:
        if instance.game_id == "Mario_Kart":
            winnaar = instance.winnaar
            instance.winnaar.totalScoreMarioKart += 3
            instance.winnaar.save()

#----------------------------------------------------------------------#

        if instance.game_id == "Fifa":
            winnaar = instance.winnaar
            instance.winnaar.totalScoreFifa += 3
            instance.winnaar.save()

#----------------------------------------------------------------------#

        if instance.game_id == "Rocket_League":
            winnaar = instance.winnaar
            instance.winnaar.totalScoreRocketLeague += 3
            instance.winnaar.save()

#----------------------------------------------------------------------#

        if instance.game_id == "Versus":
            winnaar = instance.winnaar
            instance.winnaar.totalScoreVersus += 3
            instance.winnaar.save()



@receiver(post_save, sender=TeamWedstrijden)
def updateTotalScore(sender, instance, created, **kwargs):
    if created:
        if instance.game_id == "Versus":
            team = instance.team
            score = instance.score

            if instance.score > instance.team.totalTeamScoreVersus:
             instance.team.totalTeamScoreVersus = instance.score
             instance.team.save()

#----------------------------------------------------------------------#

        if instance.game_id == "Qub3z_Shooter":
            team = instance.team
            score = instance.score

            if instance.score > instance.team.totalTeamScoreQub3zShooter:
             instance.team.totalTeamScoreQub3zShooter = instance.score
             instance.team.save()

#----------------------------------------------------------------------#

        if instance.game_id == "Cyber_Shock":
            team = instance.team
            score = instance.score

            if instance.score > instance.team.totalTeamScoreCyberShock:
             instance.team.totalTeamScoreCyberShock = instance.score
             instance.team.save()

#----------------------------------------------------------------------#

        if instance.game_id == "Dead_Ahead":
            team = instance.team
            score = instance.score

            if instance.score > instance.team.totalTeamScoreDeadAhead:
             instance.team.totalTeamScoreDeadAhead = instance.score
             instance.team.save()

#----------------------------------------------------------------------#

        if instance.game_id == "Arrow_Song":
            team = instance.team
            score = instance.score

            if instance.score > instance.team.totalTeamScoreArrowSong:
             instance.team.totalTeamScoreArrowSong = instance.score
             instance.team.save()

#----------------------------------------------------------------------#

        if instance.game_id == "Quantum_Arena":
            team = instance.team
            score = instance.score

            if instance.score > instance.team.totalTeamScoreQuantumArena:
             instance.team.totalTeamScoreQuantumArena = instance.score
             instance.team.save()
