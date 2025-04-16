from django.contrib import admin

from users.models.auth import TimedAuthToken
from users.models.users import CustomUser

admin.site.register(CustomUser)
admin.site.register(TimedAuthToken)
