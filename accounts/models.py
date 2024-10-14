from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.db import models
import re


STANDING_CHOICES = [
('freshman', 'Freshman'),
('sophomore', 'Sophomore'),
('junior', 'Junior'),
('senior', 'Senior'),
('postgraduate', 'Postgraduate'),
]


class Classes(models.Model):
    cSCI_Alphanumeric = models.CharField(max_length=100, unique=True)
    class_title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.cSCI_Alphanumeric

    def clean(self):
        pattern = r'^CSCI \d{3}$'
        if not re.match(pattern, self.cSCI_Alphanumeric):
            raise ValidationError(
                gettext_lazy('Class name must be in the form "CSCI ###" where ### is a three-digit number.'),
                code='invalid'
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

class CustomUser(AbstractUser):

    tutoring_classes = models.ManyToManyField(
        Classes,
        blank=True,
        help_text="Classes that the tutor is able to tutor (Hold down Control/Command to select more than one)"
    )
    
    first_name = models.CharField(
        max_length=50,
        help_text="First name of the tutor"
    )
    
    last_name = models.CharField(
        max_length=50,
        help_text="Last name of the tutor"
    )

    credit_standing = models.CharField(
        max_length=50,
        choices=STANDING_CHOICES,
        blank=True,
        null=True,
        help_text="Credit standing of the tutor"
    )
