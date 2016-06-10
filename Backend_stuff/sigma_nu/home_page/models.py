from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Active(models.Model):
    #each active in the fraternity
    first_name = CharField()
    last_name = CharField()
    badge_number = CharField()
    phone_number = CharField()
    email_address = EmailField()

    def __unicode__(self):
        return self.badge_number
