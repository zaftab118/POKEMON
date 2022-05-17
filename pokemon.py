import typedata
from type_advantage import type_advantages_demo
from typedata import *


def type_advantage(p1, p2):
    status_code = 3
    attack_type = typedata.types.get(p1.poke_type)
    if p2.poke_type in attack_type[0]:
        status_code = 0
    if p2.poke_type in attack_type[1]:
        status_code = 1
    if p2.poke_type in attack_type[2]:
        status_code = 2
    return status_code


class Pokemon:

    def __init__(self, name, level, poke_type):
        self.name = name
        self.level = level
        self.poke_type = poke_type.lower()
        self.max_health = level * 25
        self.health = level * 25
        self.is_knocked_out = False

    def lose_health(self, damage):
        if self.health > 0:
            if damage > self.health:
                damage = self.health
        self.health -= damage
        print('{name} took {damage} damage! Current hp is {health}.'.format(name=self.name, damage=damage,
                                                                                health=self.health))
        print("----------------------------------------------------------------------------")

        if self.health <= 0:
            self.knocked_out()

    def gain_health(self, heal):
        if self.health > 0:
            self.health += heal
            print('{name} healed {heal} hp. Current hp is {health}.'.format(name=self.name, heal=heal,
                                                                            health=self.health))
        else:
            self.knocked_out()

    def knocked_out(self):
        if self.health == 0:
            self.is_knocked_out = True
            print('{name} is knocked out.'.format(name=self.name))

    def revive(self):
        if self.is_knocked_out == True:
            self.is_knocked_out = False
            self.health += self.max_health / 2
            print('{name} is fully healed and ready to battle!'.format(name=self.name))

    def max_revive(self):
        if self.is_knocked_out == True:
            self.is_knocked_out = False
            self.health += self.max_health
            print('{name} is fully healed and ready to battle!'.format(name=self.name))

    def attack(self, other_pokemon):
        damage = 0
        attack_effectiveness = type_advantage(self, other_pokemon)
        if self.health > 0 and other_pokemon.health > 0:
            if attack_effectiveness == 0:
                damage = self.level * 2
                if damage > other_pokemon.health:
                    damage = other_pokemon.health
                print('That move was super effective! {name} dealt {damage} damage to {other_pokemon}!'.format(
                    name=self.name,
                    damage=damage, other_pokemon=other_pokemon.name))
                other_pokemon.lose_health(damage)
            elif attack_effectiveness == 1:
                damage = self.level
                if damage > other_pokemon.health:
                    damage = other_pokemon.health
                print('{name} dealt {damage} damage to {other_pokemon}.'.format(name=self.name, damage=damage,
                                                                                other_pokemon=other_pokemon.name))
                other_pokemon.lose_health(damage)
            elif attack_effectiveness == 2:
                damage = self.level / 2
                if damage > other_pokemon.health:
                    damage = other_pokemon.health
                print('That move was not very effective. {name} dealt {damage} damage to {other_pokemon}.'.format(
                    name=self.name,
                    damage=damage, other_pokemon=other_pokemon.name))
                other_pokemon.lose_health(damage)
            elif attack_effectiveness == 3:
                print('No effect.')


charizard = Pokemon('Charizard', 40, 'Fire')
infernape = Pokemon('Infernape', 40, 'Fire')
moltres = Pokemon('Moltres', 40, 'Fire')
arcanine = Pokemon('Arcanine', 40, 'Bug')
venosaur = Pokemon('Venosaur', 40, 'Grass')
sprigatito = Pokemon('Sprigatito', 40, 'Ice')
sceptile = Pokemon('Sceptile', 40, 'Grass')
rillaboom = Pokemon('Rillaboom', 40, 'Grass')
garydos = Pokemon('Garydos', 40, 'Steel')
empoleon = Pokemon('Empoleon', 40, 'Water')
blastoise = Pokemon('Blastoise', 40, 'Psychic')
suicune = Pokemon('Suicune', 40, 'Ghost')

# charizard.attack(blastoise)
# empoleon.attack(charizard)