from django.contrib import admin
from .models import Leave, Season, UserSeason

admin.site.register(Leave)
admin.site.register(Season)
admin.site.register(UserSeason)
