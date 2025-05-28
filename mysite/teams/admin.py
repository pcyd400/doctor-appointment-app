from django.contrib import admin
from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')  # display these columns in the admin list

