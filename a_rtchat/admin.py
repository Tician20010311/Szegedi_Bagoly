from django.contrib import admin
from .models import *

admin.site.register(ChatGroup)
admin.site.register(GroupMessage)

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'css_path', 'is_active')
    list_editable = ('is_active',)