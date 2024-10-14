from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("tutoring_classes", "last_name", "first_name", "credit_standing")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        
        model = CustomUser
        fields = UserChangeForm.Meta.fields
