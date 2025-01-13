from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth import get_user_model
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = get_user_model()   
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ('email', 'username','age',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'age')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'username', 'age', 'password1', 'password2')}),
    )
admin.site.register(CustomUser, CustomUserAdmin)