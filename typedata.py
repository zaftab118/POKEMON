#Index 0 is super effective
#Index 1 is not very effective
#Index 2 is regular effective

types = {
    "fire": [["grass", "steel", "ice", "bug"], ["normal", "electric", "fighting", "poison", "ground", "flying", "psychic", "ghost", "dark", "fairy"], ["fire", "water", "rock", "dragon"]],
    "water": [["fire", "ground", "rock"], ["normal", "electric", "fighting", "poison", "ice", "flying", "psychic", "ghost", "dark", "fairy", "bug", "steel"], ["water", "grass", "dragon"]],
    "grass": [["water", "ground", "rock"],["normal", "electric", "ice", "fighting", "psychic", "ghost", "dark", "fairy"],["fire", "grass", "poison", "flying", "bug", "dragon", "steel"]],
    "normal": [[], ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "dragon", "dark", "fairy"],["rock", "steel"], ["ghost"]],
    "electric": [["water", "flying"], ["normal", "fire", "ice", "fighting", "poison", "psychic", "bug", "rock", "ghost", "dark", "steel", "fairy"], ["electric", "grass", "dragon"], ["ground"]],
    "ice": [["grass", "ground", "flying", "dragon"], ["normal", "electric", "fighting", "poison", "psychic", "bug", "rock", "ghost", "dark", "fairy"], ["fire", "water", "ice", "steel"]],
    "fighting": [["normal", "ice", "rock", "dark", "steel"], ["fire", "water", "electric", "grass", "fighting", "ground", "dragon"], ["poison", "flying", "psychic", "bug", "fairy"], ["ghost"]],
    "poison": [["grass", "fairy"], ["normal", "fire", "water", "electric", "ice", "fighting", "flying", "psychic", "bug", "dragon", "dark"], ["poison", "ground", "rock", "ghost"], ["steel"]],
    "ground": [["fire", "electric", "poison", "rock", "steel"], ["normal", "water", "ice", "fighting", "ground", "psychic", "ghost", "dragon", "dark", "fairy"], ["grass", "bug"], ["flying"]],
    "flying": [["grass", "fighting", "bug"], ["normal", "fire", "water", "ice", "poison", "ground", "flying", "psychic", "ghost", "dragon", "dark", "fairy"], ["electric", "rock", "steel"]],
    "psychic": [["fighting", "poison"], ["normal", "fire", "water", "electric", "grass", "ice", "ground", "flying", "bug", "rock", "ghost", "dragon", "fairy"], ["psychic", "steel"], ["dark"]],
    "bug": [["grass", "psychic", "dark"], ["normal", "water", "electric", "ice", "ground", "bug", "rock", "dragon"], ["fire", "fighting", "poison", "flying", "ghost", "steel", "fairy"]],
    "rock": [["fire", "ice", "flying", "bug"], ["normal", "water", "electric", "grass", "poison", "psychic", "rock", "ghost", "dragon", "dark", "fairy"], ["fighting", "ground", "steel"]],
    "ghost": [["psychic", "ghost"], ["fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "bug", "rock", "dragon", "steel", "fairy"], ["dark"], ["normal"]],
    "dragon": [["dragon"], ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dark"], ["steel"], ["fairy"]],
    "dark": [["psychic", "ghost"], ["normal", "fire", "water", "electric", "grass", "ice", "poison", "ground", "flying", "bug", "rock", "dragon", "steel"], ["fighting", "dark", "fairy"]],
    "steel": [["ice", "rock", "fairy"], ["normal", "grass", "fighting", "poison", "ground", "flying", "psychic", "bug", "ghost", "dragon", "dark"], ["fire", "water", "electric", "steel"]],
    "fairy": [["fighting", "dragon", "dark"], ["normal", "water", "electric", "grass", "ice", "ground", "flying", "psychic", "bug", "rock", "ghost", "fairy"], ["fire", "poison", "steel"]]
}
