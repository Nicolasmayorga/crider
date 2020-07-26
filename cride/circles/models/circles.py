"""Circles model"""

# Django

from django.db import models

# Utilities
from cride.utils.models import CRideModel

class Circle(CRideModel):
    """Circle model.

    A circle is a private group where rides are offered and taken by its members. To join a circle a user must receive an unique invitation code from an existing circle member"""

    name = models.CharField('circle name', max_length=140)

    slug_name= models.SlugField(unique=True, max_length=40)

    about = models.CharField('circle name', max_length=225)
    picture = models.ImageField(upload_to='circles/pictures', blank=True, null=True)

    # Stats
    rides_offered = models.PositiveIntegerField(default=0)

    rides_taken = models.PositiveIntegerField(default=0)

    verified = models.BooleanField(
        'verified circle',
        default=False,
        help_text='Verified cicles are also known as official communities'
    )

    is_public = models.BooleanField(
        default=True,
        help_text=' Public cicles are listed in the main page so everyone know about there existence'
    )

    is_limited = models.BooleanField(
        'limited',
        default=False,
        help_text='Limited circles can grow up to a fixed number of members. '
    )

    members_limit = models.PositiveIntegerField(
        default=0,
        help_text='If a circle is limited, this will be the limit on the number of the members'
    )

    def __str__(self):
        """Return a circle name"""
        return self.name

    class Meta(CRideModel.Meta):
        """Meta class"""

        ordering = ['-rides_taken', '-rides_offered']

