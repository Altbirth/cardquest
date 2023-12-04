from django.contrib import admin
from .models import PokemonCard
from .models import Trainer
from .models import Collection

admin.site.register (PokemonCard)
admin.site.register (Trainer)
admin.site.register (Collection)
# Register your models here.



# @admin.register(PokemonCard)
# class PokemonAdmin(admin.ModelAdmin):
#     list_display = ("name", "rarity")
#     search_fields = ("name",)
