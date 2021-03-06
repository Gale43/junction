from django.contrib.auth.models import User
from junction.base.models import AuditModel
from django.db import models


class Profile(AuditModel):
    '''
    It stores the City/Phone Details of the User.
    '''

    User._meta.get_field("first_name").max_length = 100
    User._meta.get_field("last_name").max_length = 100
    User._meta.get_field("username").max_length = 100
    User._meta.get_field("email").max_length = 100

    user = models.OneToOneField(User)
    city = models.CharField(max_length=100, blank=True, null=True)
    contact_no = models.CharField(max_length=15, blank=True, null=True)

    def __unicode__(self):
        return self.user.username
