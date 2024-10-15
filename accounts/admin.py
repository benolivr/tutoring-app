from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Classes, TutoringHour

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ["username", "first_name", "last_name", "credit_standing", "is_staff"]

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("is_TA", "tutoring_classes","credit_standing")}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
    (None, {"fields": ("is_TA", "tutoring_classes","credit_standing")}),
    )
    
class ClassesAdmin(admin.ModelAdmin):
    list_display = ["cSCI_Alphanumeric", "class_title"]
    search_fields = ["cSCI_Alphanumeric", "class_title"]

class TutoringHourAdmin(admin.ModelAdmin):
    list_display = ["user", "day", "hour"]
    search_fields = ["user__username", "day", "hour"]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Classes, ClassesAdmin)
admin.site.register(TutoringHour, TutoringHourAdmin)