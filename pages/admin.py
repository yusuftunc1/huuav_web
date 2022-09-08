from django.contrib import admin
from .models import announcements, teams, teammembers, managers,sponsors

# Register your models here.

class announcementAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_per_page = 20
    list_display_links = ('title',)


class teamAdmin(admin.ModelAdmin):
    list_display = ('teamname','id')
    search_fields = ('teamname',)
    list_per_page = 20
    list_display_links = ('teamname',)

class teammembersAdmin(admin.ModelAdmin):
    list_display = ('teamname','role','name','email','linkedin')
    search_fields = ('teamname',)
    list_per_page = 20
    list_display_links = ('teamname','name')

class managersAdmin(admin.ModelAdmin):
    list_display = ('name','role','display')
    search_fields = ('teamname',)
    list_per_page = 20
    list_display_links = ('name',)


class sponsorsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 20
    list_display_links = ('name',)


admin.site.register(announcements,announcementAdmin)
admin.site.register(teams,teamAdmin)
admin.site.register(teammembers,teammembersAdmin)
admin.site.register(managers, managersAdmin)
admin.site.register(sponsors,sponsorsAdmin)
