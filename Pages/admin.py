from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def Photo(self, object):
        return format_html('<img src="{}" style="border-radius: 50px;" width="40" />', format(object.photo.url))
    list_display = ("id", "Photo", "first_name", "last_name", "designation", "date")
    list_display_links = ("first_name", "last_name", "Photo")
    search_fields = ("id", "first_name", "last_name", "designation", "date")
    list_filter = ('designation', )


admin.site.register(Team, TeamAdmin)