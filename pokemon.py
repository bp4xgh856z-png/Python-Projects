import random
print('''A wild Charmander has appeared! 
Go, Pikachu! 

Choose your attack: 
1. Thundershock 
2. Tackle ''')

choice = input('')

pokemon_name = 'Pikachu'
pokemon_hp = 100
pokemon_attack = 20
pokemon_speed = 20

pokemon_name2 = 'Charmander'
pokemon_hp2 = 100
pokemon_attack2 = 15
pokemon_speed2 = 30
while pokemon_hp > 0 and pokemon_hp2 > 0:
    if choice in ('1', '2'):
        roll = random.randint(1,100)
        if roll >= pokemon_speed2:
            pokemon_hp2 = pokemon_hp2 - pokemon_attack
            print(f'''Your attack hits! 
            Charmander is at {pokemon_hp2} HP...''')
            if pokemon_hp2 <= 0:
                print('Charmander has fainted! You have won.')
                break
        else:
            print(f'{pokemon_name2} dodged the attack!')

    roll_2 = random.randint(1, 100)
    if roll_2 >= pokemon_speed:
        pokemon_hp = pokemon_hp - pokemon_attack2
        print(f'''
        Charmander uses ember! 
        Pikachu is at {pokemon_hp} hp...''')
        if pokemon_hp <= 0:
            print('Pikachu has fainted...')
            break
    else:
        print('''Charmander used Ember! 
        Pikachu avoided the attack!''')
    choice = input('''
    Choose your attack 
    1. Thundershock 
    2. Tackle''')


