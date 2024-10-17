from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.db import models
import re
from datetime import time


STANDING_CHOICES = [
('Freshman', 'Freshman'),
('Sophomore', 'Sophomore'),
('Junior', 'Junior'),
('Senior', 'Senior'),
('Postgraduate', 'Postgraduate'),
]

HOUR_CHOICES = [
    (time(7, 0), '7:00 AM'),
    (time(8, 0), '8:00 AM'),
    (time(9, 0), '9:00 AM'),
    (time(10, 0), '10:00 AM'),
    (time(11, 0), '11:00 AM'),
    (time(12, 0), '12:00 PM'),
    (time(13, 0), '1:00 PM'),
    (time(14, 0), '2:00 PM'),
    (time(15, 0), '3:00 PM'),
    (time(16, 0), '4:00 PM'),
    (time(17, 0), '5:00 PM'),
    (time(18, 0), '6:00 PM'),
    (time(19, 0), '7:00 PM'),
    (time(20, 0), '8:00 PM'),
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
    
    is_TA = models.BooleanField(
        default=False,
        help_text="Is the user a TA?",
        )

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

class TutoringHour(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday')
    ])
    hour = models.TimeField(choices=HOUR_CHOICES)
