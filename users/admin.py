from django.contrib import admin

from users.models.users import CustomUser

admin.site.register(CustomUser)
