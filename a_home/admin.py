from django.contrib import admin
from .models import *

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):  
    list_display = ('title','description','tag','created_at','image')

@admin.register(Parents)
class ParentsAdmin(admin.ModelAdmin):
    list_display = ('text','link')

@admin.register(LeadNews)
class LeadNewsAdmin(admin.ModelAdmin):
    list_display = ('created_at','title','description','image')


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'css_path', 'is_active')
    list_editable = ('is_active',)

@admin.register(Withoutborders)
class WithoutbordersAdmin(admin.ModelAdmin):
    list_display = ('created_at','title','description','link_to')

@admin.register(Firstday)
class FirstdayAdmin(admin.ModelAdmin):
    list_display = ('image',)

@admin.register(Secondday)
class SecondAdmin(admin.ModelAdmin):
    list_display = ('image',)

@admin.register(Thirdday)
class ThirdAdmin(admin.ModelAdmin):
    list_display = ('image',)

@admin.register(Fourthday)
class FifthAdmin(admin.ModelAdmin):
    list_display = ('image',)

@admin.register(Fiftday)
class FifthAdmin(admin.ModelAdmin):
    list_display = ('image',)
# Register your models here.
