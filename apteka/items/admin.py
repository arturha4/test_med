from django.contrib import admin
from .models import Tovar, ClientTovar, MatchedTovar

@admin.register(Tovar)
class TovarAdmin(admin.ModelAdmin):
    list_display = ('name_prep', 'ean13')


@admin.register(ClientTovar)
class ClientTovarAdmin(admin.ModelAdmin):
    list_display = ('name_prep', 'ean13')


@admin.register(MatchedTovar)
class MatchedTovarAdmin(admin.ModelAdmin):
    list_display = ('tovar','show_client_tovars', 'quantity')
    filter_horizontal = ('client_tovars',)

    def show_client_tovars(self, obj):
        return ", ".join([a.name_prep for a in obj.client_tovars.all()])

