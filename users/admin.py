from django.contrib import admin
from .models import  Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'location', 'birth_date')
    search_fields = ('user__username', 'user__email', 'location')

admin.site.register(Profile, ProfileAdmin)