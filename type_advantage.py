def type_advantages_demo(p1, p2):
    poketypes = [
        'normal', 'fire', 'water', 'electric', 'grass', 'ice', 'fighting', 'poison', 'ground', 'flying', 'psychic',
        'bug', 'rock', 'ghost', 'dragon', 'dark', 'steel', 'fairy'
    ]
    status_code = 0
    while p1.poke_type == 'fire':
        if p2.poke_type == 'grass' \
                or p2.poke_type == 'ice' \
                or p2.poke_type == 'bug' \
                or p2.poke_type == 'steel':
            status_code = 3
            break
        if p2.poke_type == 'normal' \
                or p2.poke_type == 'electric' \
                or p2.poke_type == 'fighting' \
                or p2.poke_type == 'poison' \
                or p2.poke_type == 'ground' \
                or p2.poke_type == 'flying' \
                or p2.poke_type == 'psychic' \
                or p2.poke_type == 'ghost' \
                or p2.poke_type == 'dark' \
                or p2.poke_type == 'fairy':
            status_code = 2
            break
        if p2.poke_type == 'fire' \
                or p2.poke_type == 'water' \
                or p2.poke_type == 'rock' \
                or p2.poke_type == 'dragon':
            status_code = 1
            break
    while p1.poke_type == 'water':
        if p2.poke_type == 'fire' \
                or p2.poke_type == 'ground' \
                or p2.poke_type == 'rock':
            status_code = 3
            break
        if p2.poke_type == 'normal' \
                or p2.poke_type == 'electric' \
                or p2.poke_type == 'ice' \
                or p2.poke_type == 'fighting' \
                or p2.poke_type == 'poison' \
                or p2.poke_type == 'flying' \
                or p2.poke_type == 'psychic' \
                or p2.poke_type == 'bug' \
                or p2.poke_type == 'ghost' \
                or p2.poke_type == 'dark' \
                or p2.poke_type == 'steel' \
                or p2.poke_type == 'fairy':
            status_code = 2
            break
        if p2.poke_type == 'water' \
                or p2.poke_type == 'grass' \
                or p2.poke_type == 'dragon':
            status_code = 1
            break
    while p1.poke_type == 'grass':
        if p2.poke_type == 'water' \
                or p2.poke_type == 'ground' \
                or p2.poke_type == 'rock':
            status_code = 3
            break
        if p2.poke_type == 'normal' \
                or p2.poke_type == 'electric' \
                or p2.poke_type == 'ice' \
                or p2.poke_type == 'fighting' \
                or p2.poke_type == 'psychic' \
                or p2.poke_type == 'ghost' \
                or p2.poke_type == 'dark' \
                or p2.poke_type == 'fairy':
            status_code = 2
            break
        if p2.poke_type == 'fire' \
                or p2.poke_type == 'grass' \
                or p2.poke_type == 'poison' \
                or p2.poke_type == 'flying' \
                or p2.poke_type == 'bug' \
                or p2.poke_type == 'dragon' \
                or p2.poke_type == 'steel':
            status_code = 1
            break
    while p1.poke_type == 'normal':
        if p2.poke_type == '':
            status_code = 3
            break
        if p2.poke_type == 'normal' \
                or p2.poke_type == 'fire' \
                or p2.poke_type == 'water' \
                or p2.poke_type == 'electric' \
                or p2.poke_type == 'grass'\
                or p2.poke_type == 'ice' \
                or p2.poke_type == 'fighting' \
                or p2.poke_type == 'poison' \
                or p2.poke_type == 'ground' \
                or p2.poke_type == 'flying' \
                or p2.poke_type == 'psychic' \
                or p2.poke_type == 'bug' \
                or p2.poke_type == 'dragon' \
                or p2.poke_type == 'dark' \
                or p2.poke_type == 'fairy':
            status_code = 2
            break
        if p2.poke_type == 'rock' \
                or p2.poke_type == 'steel':
            status_code = 1
            break
        if p2.poke_type == 'ghost':
            status_code = 0
            break
    while p1.poke_type == 'electric':
        if p2.poke_type == 'water' \
                or p2.poke_type == 'flying':
            status_code = 3
            break
        if p2.poke_type == 'normal' \
                or p2.poke_type == 'fire' \
                or p2.poke_type == 'ice'\
                or p2.poke_type == 'fighting' \
                or p2.poke_type == 'poison' \
                or p2.poke_type == 'psychic' \
                or p2.poke_type == 'bug' \
                or p2.poke_type == 'rock' \
                or p2.poke_type == 'ghost' \
                or p2.poke_type == 'dark' \
                or p2.poke_type == 'steel' \
                or p2.poke_type == 'fairy':
            status_code = 2
            break
        if p2.poke_type == 'electric' \
                or p2.poke_type == 'grass' \
                or p2.poke_type == 'dragon':
            status_code = 1
            break
        if p2.poke_type == 'ground':
            status_code = 0
            break
    while p1.poke_type == 'ice':
        if p2.poke_type == 'grass' \
                or p2.poke_type == 'ground' \
                or p2.poke_type == 'flying' \
                or p2.poke_type == 'dragon':
            status_code = 3
            break
        if p2.poke_type == 'normal' \
                or p2.poke_type == 'electric' \
                or p2.poke_type == 'fighting' \
                or p2.poke_type == 'poison' \
                or p2.poke_type == 'psychic' \
                or p2.poke_type == 'bug' \
                or p2.poke_type == 'rock' \
                or p2.poke_type == 'ghost' \
                or p2.poke_type == 'dark'\
                or p2.poke_type == 'fairy':
            status_code = 2
            break
        if p2.poke_type == 'fire' \
                or p2.poke_type == 'water' \
                or p2.poke_type == 'ice' \
                or p2.poke_type == 'steel':
            status_code = 1
            break
    while p1.poke_type == 'fighting':
        if p2.poke_type == 'normal'\
                or p2.poke_type == 'ice' \
                or p2.poke_type == 'rock' \
                or p2.poke_type == 'dark'\
                or p2.poke_type == 'steel':
            status_code = 3
            break
        if p2.poke_type == 'fire'\
                or p2.poke_type == 'water' \
                or p2.poke_type == 'electric' \
                or p2.poke_type == 'grass' \
                or p2.poke_type == 'fighting' \
                or p2.poke_type == 'ground' \
                or p2.poke_type == 'dragon':
            status_code = 2
            break
        if p2.poke_type == 'poison' \
                or p2.poke_type == 'flying' \
                or p2.poke_type == 'psychic' \
                or p2.poke_type == 'bug' \
                or p2.poke_type == 'fairy':
            status_code = 1
            break
        if p2.poke_type == 'ghost':
            status_code = 0
            break
    while p1.poke_type == 'poison':
        if p2.poke_type == 'grass' \
                or p2.poke_type == 'fairy':
            status_code = 3
            break
        if p2.poke_type == 'normal' \
                or p2.poke_type == 'fire' \
                or p2.poke_type == 'water'\
                or p2.poke_type == 'electric' \
                or p2.poke_type == 'ice' \
                or p2.poke_type == 'fighting' \
                or p2.poke_type == 'flying' \
                or p2.poke_type == 'psychic' \
                or p2.poke_type == 'bug' \
                or p2.poke_type == 'dragon' \
                or p2.poke_type == 'dark':
            status_code = 2
            break
        if p2.poke_type == 'poison' \
                or p2.poke_type == 'ground' \
                or p2.poke_type == 'rock'\
                or p2.poke_type == 'ghost':
            status_code = 1
            break
        if p2.poke_type == 'steel':
            status_code = 0
            break
    while p1.poke_type == 'ground':
        if p2.poke_type == 'fire' \
                or p2.poke_type == 'electric' \
                or p2.poke_type == 'poison'\
                or p2.poke_type == 'rock'\
                or p2.poke_type == 'steel':
            status_code = 3
            break
        if p2.poke_type == 'normal'\
                or p2.poke_type == 'water' \
                or p2.poke_type == 'ice' \
                or p2.poke_type == 'fighting' \
                or p2.poke_type == 'ground' \
                or p2.poke_type == 'psychic' \
                or p2.poke_type == 'ghost' \
                or p2.poke_type == 'dragon' \
                or p2.poke_type == 'dark' \
                or p2.poke_type == 'fairy':
            status_code = 2
            break
        if p2.poke_type == 'grass' \
                or p2.poke_type == 'bug':
            status_code = 1
            break
        if p2.poke_type == 'flying':
            status_code = 0
            break
    while p1.poke_type == 'flying':
        if p2.poke_type == 'grass' \
                or p2.poke_type == 'fighting' \
                or p2.poke_type == 'bug':
            status_code = 3
            break
        if p2.poke_type == 'normal' \
                or p2.poke_type == 'fire'\
                or p2.poke_type == 'water' \
                or p2.poke_type == 'ice' \
                or p2.poke_type == 'poison' \
                or p2.poke_type == 'ground' \
                or p2.poke_type == 'flying' \
                or p2.poke_type == 'psychic' \
                or p2.poke_type == 'ghost' \
                or p2.poke_type == 'dragon' \
                or p2.poke_type == 'dark' \
                or p2.poke_type == 'fairy':
            status_code = 2
            break
        if p2.poke_type == 'electric' \
                or p2.poke_type == 'rock' \
                or p2.poke_type == 'steel':
            status_code = 1
            break
    while p1.poke_type == 'psychic':
        if p2.poke_type == 'fighting' \
                or p2.poke_type == 'poison':
            status_code = 3
            break
        if p2.poke_type == 'normal'\
                or p2.poke_type == 'fire' \
                or p2.poke_type == 'water' \
                or p2.poke_type == 'electric'\
                or p2.poke_type == 'grass' \
                or p2.poke_type == 'ice' \
                or p2.poke_type == 'ground' \
                or p2.poke_type == 'flying' \
                or p2.poke_type == 'bug' \
                or p2.poke_type == 'rock' \
                or p2.poke_type == 'ghost' \
                or p2.poke_type == 'dragon' \
                or p2.poke_type == 'fairy':
            status_code = 2
            break
        if p2.poke_type == 'psychic' \
                or p2.poke_type == 'steel':
            status_code = 1
            break
        if p2.poke_type == 'dark':
            status_code = 0
            break
    while p1.poke_type == 'bug':
        if p2.poke_type == 'grass'\
                or p2.poke_type == 'psychic' \
                or p2.poke_type == 'dark':
            status_code = 3
            break
        if p2.poke_type == 'normal' \
                or p2.poke_type == 'water' \
                or p2.poke_type == 'electric' \
                or p2.poke_type == 'ice' \
                or p2.poke_type == 'ground' \
                or p2.poke_type == 'bug' \
                or p2.poke_type == 'rock'\
                or p2.poke_type == 'dragon':
            status_code = 2
            break
        if p2.poke_type == 'fire' \
                or p2.poke_type == 'fighting' \
                or p2.poke_type == 'poison' \
                or p2.poke_type == 'flying' \
                or p2.poke_type == 'ghost' \
                or p2.poke_type == 'steel' \
                or p2.poke_type == 'fairy':
            status_code = 1
            break
    while p1.poke_type == 'rock':
        if p2.poke_type == 'fire' \
                or p2.poke_type == 'ice'\
                or p2.poke_type == 'flying' \
                or p2.poke_type == 'bug':
            status_code = 3
            break
        if p2.poke_type == 'normal' \
                or p2.poke_type == 'water' \
                or p2.poke_type == 'electric' \
                or p2.poke_type == 'grass' \
                or p2.poke_type == 'poison'\
                or p2.poke_type == 'psychic' \
                or p2.poke_type == 'rock'\
                or p2.poke_type == 'ghost' \
                or p2.poke_type == 'dragon' \
                or p2.poke_type == 'dark' \
                or p2.poke_type == 'fairy':
            status_code = 2
            break
        if p2.poke_type == 'fighting' \
                or p2.poke_type == 'ground' \
                or p2.poke_type == 'steel':
            status_code = 1
            break
    while p1.poke_type == 'ghost':
        if p2.poke_type == 'psychic' \
                or p2.poke_type == 'ghost':
            status_code = 3
            break
        if p2.poke_type == 'fire' \
                or p2.poke_type == 'water' \
                or 'element' \
                or p2.poke_type == 'electric' \
                or p2.poke_type == 'grass' \
                or p2.poke_type == 'ice' \
                or p2.poke_type == 'fighting'\
                or p2.poke_type == 'poison' \
                or p2.poke_type == 'ground' \
                or p2.poke_type == 'flying' \
                or p2.poke_type == 'bug' \
                or p2.poke_type == 'rock' \
                or p2.poke_type == 'dragon' \
                or p2.poke_type == 'steel' \
                or p2.poke_type == 'fairy':
            status_code = 2
            break
        if p2.poke_type == 'dark':
            status_code = 1
            break
        if p2.poke_type == 'normal':
            status_code = 0
            break
    while p1.poke_type == 'dragon':
        if p2.poke_type == 'dragon':
            status_code = 3
            break
        if p2.poke_type == 'normal' \
                or p2.poke_type == 'fire' \
                or p2.poke_type == 'water' \
                or p2.poke_type == 'electric' \
                or p2.poke_type == 'grass' \
                or p2.poke_type == 'ice' \
                or p2.poke_type == 'fighting' \
                or p2.poke_type == 'poison' \
                or p2.poke_type == 'ground' \
                or p2.poke_type == 'flying' \
                or p2.poke_type == 'psychic' \
                or p2.poke_type == 'bug' \
                or p2.poke_type == 'rock' \
                or p2.poke_type == 'ghost' \
                or p2.poke_type == 'dark':
            status_code = 2
            break
        if p2.poke_type == 'steel':
            status_code = 1
            break
        if p2.poke_type == 'fairy':
            status_code = 0
            break
    while p1.poke_type == 'dark':
        if p2.poke_type == 'psychic' \
                or p2.poke_type == 'ghost':
            status_code = 3
            break
        if p2.poke_type == 'normal' \
                or p2.poke_type == 'fire' \
                or p2.poke_type == 'water' \
                or p2.poke_type == 'electric' \
                or p2.poke_type == 'grass' \
                or p2.poke_type == 'ice' \
                or p2.poke_type == 'poison'\
                or p2.poke_type == 'ground' \
                or p2.poke_type == 'flying' \
                or p2.poke_type == 'bug' \
                or p2.poke_type == 'rock' \
                or p2.poke_type == 'dragon' \
                or p2.poke_type == 'steel':
            status_code = 2
            break
        if p2.poke_type == 'fighting' \
                or p2.poke_type == 'dark' \
                or p2.poke_type == 'fairy':
            status_code = 1
            break
    while p1.poke_type == 'steel':
        if p2.poke_type == 'ice' \
                or p2.poke_type == 'rock' \
                or p2.poke_type == 'fairy':
            status_code = 3
            break
        if p2.poke_type == 'normal' \
                or p2.poke_type == 'grass' \
                or p2.poke_type == 'fighting' \
                or p2.poke_type == 'poison' \
                or p2.poke_type == 'ground' \
                or p2.poke_type == 'flying' \
                or p2.poke_type == 'psychic' \
                or p2.poke_type == 'bug' \
                or p2.poke_type == 'ghost' \
                or p2.poke_type == 'dragon' \
                or p2.poke_type == 'dark':
            status_code = 2
            break
        if p2.poke_type == 'fire' \
                or p2.poke_type == 'water' \
                or p2.poke_type == 'electric' \
                or p2.poke_type == 'steel':
            status_code = 1
            break
    while p1.poke_type == 'fairy':
        if p2.poke_type == 'fighting' \
                or p2.poke_type == 'dragon' \
                or p2.poke_type == 'dark':
            status_code = 3
            break
        if p2.poke_type == 'normal' \
                or p2.poke_type == 'water' \
                or p2.poke_type == 'electric' \
                or p2.poke_type == 'grass' \
                or p2.poke_type == 'ice' \
                or p2.poke_type == 'ground' \
                or p2.poke_type == 'flying' \
                or p2.poke_type == 'psychic' \
                or p2.poke_type == 'bug' \
                or p2.poke_type == 'rock' \
                or p2.poke_type == 'ghost' \
                or p2.poke_type == 'fairy':
            status_code = 2
            break
        if p2.poke_type == 'fire' \
                or p2.poke_type == 'poison' \
                or p2.poke_type == 'steel':
            status_code = 1
            break
    return status_code