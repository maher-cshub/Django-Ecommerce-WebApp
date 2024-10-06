from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from userauths.models import User
from .models import User


# Register your models here.


admin.site.register(User)