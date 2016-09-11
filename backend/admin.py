from django.contrib import admin

# Register your models here.
from backend.models import *

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

class RequestsAdmin(admin.ModelAdmin):
    list_display = ('item', 'client_profile')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',)

class InteractionAdmin(admin.ModelAdmin):
    list_display = ('user', 'client', 'location', 'timestamp', 'description')

admin.site.register(CustomUser, CustomUserAdmin)
#admin.site.register(Client, ClientAdmin)
admin.site.register(Requests, RequestsAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Interaction, InteractionAdmin)

