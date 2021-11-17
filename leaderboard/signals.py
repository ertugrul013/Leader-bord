from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Customer, Matche

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