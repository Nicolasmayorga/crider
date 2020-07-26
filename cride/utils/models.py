"""Django models utilities"""

# Django
from django.db import models

class CRideModel(models.Model):
    """Comparte Ride base model

    CrideModel acts as an abstract base class from which every other model in the project will inherit. This class provides every table with the following atributes:
        + created (datetime): Store the datetime the object was created
        + modified (datetime): Store the datetime the object was modified
        """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on wich the object was created'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on wich the object was last modified'
    )

    class Meta:
        """Meta options"""
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']
