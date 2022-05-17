from pokemon import Pokemon


class Trainer:
    potion_heal_value = 75
    currently_active = 0

    def __init__(self, name, p1=None, p2=None, p3=None, p4=None, p5=None, p6=None):
        self.party = [p1, p2, p3, p4, p5, p6]
        self.name = name
        self.current_pokemon = p1
        self.potion_count = 3
        self.whited_out = False

    def use_potion(self, pokemon):
        if pokemon.health > 0:
            difference = pokemon.max_health - pokemon.health

            if difference <= 75 and difference != 0:
                print('{name} used a potion.'.format(name=self.name))
                self.potion_heal_value = difference
                pokemon.gain_health(self.potion_heal_value)
                self.potion_heal_value = 75

            elif difference == 0:
                print('Cannot use potion! {name} is already at max health.'.format(name=self.current_pokemon.name))

            else:
                print('{name} used a potion.'.format(name=self.name))
                pokemon.gain_health(self.potion_heal_value)

    def declare_attack(self, other_trainer):
        if other_trainer.current_pokemon.health > 0 and self.current_pokemon.health > 0:
            print('{name}\'s {p1} attacked {other_trainer}\'s {p2}'.format(name=self.name,
                                                                           p1=self.current_pokemon.name,
                                                                           other_trainer=other_trainer.name,
                                                                           p2=other_trainer.current_pokemon.name))
            print("----------------------------------------------------------------------------")
            self.current_pokemon.attack(other_trainer.current_pokemon)

    def switch_pokemon(self, new_pokemon):
        if new_pokemon.health > 0:
            previous_pokemon = self.current_pokemon
            self.currently_active = self.party.index(new_pokemon)
            self.current_pokemon = self.party[self.currently_active]
            print("...")
            print('{trainer} switched out {current_pokemon} for {new_pokemon}!'.format(trainer=self.name, current_pokemon=previous_pokemon.name, new_pokemon=self.current_pokemon.name, ))
        else:
            print('Can\'t switch! {new_pokemon} is currently knocked out!'.format(new_pokemon=new_pokemon.name))


charizard = Pokemon('Charizard', 40, 'Fire')
infernape = Pokemon('Infernape', 40, 'Fire')
moltres = Pokemon('Moltres', 40, 'Fire')
empoleon = Pokemon('Empoleon', 40, 'Water')
blastoise = Pokemon('Blastoise', 40, 'Water')
suicune = Pokemon('Suicune', 1, 'Water')
zohaib = Trainer('Zohaib', charizard, blastoise, moltres)
# zohaib.switch_pokemon(infernape)
# print(empoleon.max_health)

sharbreh = Trainer('Sharjy', suicune, empoleon, infernape)
zohaib.declare_attack(sharbreh)
zohaib.declare_attack(sharbreh)
sharbreh.switch_pokemon(infernape)
sharbreh.switch_pokemon(suicune)