from django.contrib import admin
from .models import PokemonCard, Trainer, Collection
# Register your models here.
class BaseModelAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'updated_at')

class TrainerAdmin(BaseModelAdmin):
    list_display = ('name', 'birthdate', 'location', 'email', 'created_at', 'updated_at')
    
class PokemonCardAdmin(BaseModelAdmin):
    list_display = (
        'name', 'rarity', 'hp', 'card_type', 'attack', 'description', 'weakness',
        'card_number', 'release_date', 'evolution_stage', 'abilities', 'created_at', 'updated_at'
    )

class CollectionAdmin(BaseModelAdmin):
    list_display = ('card', 'trainer', 'collection_date', 'created_at', 'updated_at')

# Register your models here.
admin.site.register(PokemonCard, PokemonCardAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Collection, CollectionAdmin)