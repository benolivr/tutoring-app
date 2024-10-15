from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.conf import settings
from django.contrib.auth.hashers import check_password
from .models import CustomUser, TutoringHour, Classes, HOUR_CHOICES
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class CustomUserCreationForm(UserCreationForm):
    code = forms.CharField(max_length=100, required=True, help_text="Enter the registration code")

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("is_TA", "tutoring_classes", "first_name", "last_name", "credit_standing", "code")

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if not check_password(code, settings.PREDETERMINED_CODE_HASH):
            raise forms.ValidationError("Incorrect code")
        return code

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class TutoringHourForm(forms.ModelForm):
    hour = forms.ChoiceField(choices=HOUR_CHOICES)
    class Meta:
        model = TutoringHour
        fields = ['day', 'hour']

class UpdateClassesForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['tutoring_classes']

    def __init__(self, *args, **kwargs):
        super(UpdateClassesForm, self).__init__(*args, **kwargs)
        self.fields['tutoring_classes'].queryset = Classes.objects.all()
        self.fields['tutoring_classes'].label = 'Select the classes you are able to tutor'
        self.fields['tutoring_classes'].widget = forms.CheckboxSelectMultiple()
        self.fields['tutoring_classes'].help_text = None
        self.fields['tutoring_classes'].choices = [
            (cls.id, f"{cls.cSCI_Alphanumeric} - {cls.class_title}") for cls in Classes.objects.all().order_by('cSCI_Alphanumeric')
        ]
