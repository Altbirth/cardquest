from django.core.management.base import BaseCommand
from cardquest.models import PokemonCard, Trainer

class Command(BaseCommand):
    help = 'Create initial data for the application' 

    def handle(self, *args, **kwargs):
        self.create_pokemon_cards()
        self.create_trainer()

    def create_pokemon_cards (self):
        card1 = PokemonCard(name="Pikachu", rarity="Rare",hp=60, card_type="Electric", attack="Thunder Shock",
                    description="A mouse-like pokemon that can generate electricity.",
                    weakness="Ground", card_number=25, release_date="1996-02-27", evolution_stage="Basic",
                    abilities="Static")
        card2 = PokemonCard(name= "Charmeleon", rarity= "Rare",hp= 120, card_type= "Fire", attack= "Flamethrower", 
                    description= "It has a barbaric nature. In battle, it whips its fiery tail around and slashes away with sharp claws.", 
                    weakness= "Water",card_number= 5,release_date= "1996-02-27", evolution_stage= "Stage 2", abilities= "Solar Power")

        card1.save()
        card2.save()
        self.stdout.write(self.style.SUCCESS('Successfully created Pokemon cards. '))

    def create_trainer (self):
        trainer1 = Trainer(name="Altbirth", birthdate= "1987-05-22",location= "Pallet Town",email= "ash@pokemon.com") 
        trainer1.save()
        self.stdout.write(self.style.SUCCESS('Successfully created Trainer'))

