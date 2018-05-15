from django.contrib import admin
from .models import Attandance


class AttandanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'enter_at', 'out_at', 'total_time']

admin.site.register(Attandance, AttandanceAdmin)
