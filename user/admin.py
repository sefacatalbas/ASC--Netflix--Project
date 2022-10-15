from django.contrib import admin
from .models import * # Varan 55

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','isim', 'user', 'slug')
    list_display_links = ('id', 'user')
    search_fields = ('isim',)
    list_editable = ('isim',)
    list_per_page = 10
    list_filter = ('isim', 'user')
    readonly_fields = ('slug',)
    
# Register your models here.

admin.site.register(Profile, ProfileAdmin) # Varan 56
admin.site.register(Account)