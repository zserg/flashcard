from django.contrib import admin

from api.models import Deck

class DeckAdmin(admin.ModelAdmin):
        pass

admin.site.register(Deck, DeckAdmin)

