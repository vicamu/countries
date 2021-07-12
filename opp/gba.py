from pokemons import *
import random

print("POKEMON".center(50, "-"))
print("Oak: Select your first pokemon...")
[print(f"{i+1}. {pokemon.name}") for i, pokemon in enumerate(pokemons)]
user = int(input("Choose: ")) - 1
pokemon_a = pokemons[user]
pokemons.remove(pokemon_a)
pokemon_d = random.choice(pokemons)
print(f"You rival is {pokemon_d.name}")

while pokemon_d.is_alive and pokemon_a.is_alive:
    
    for i, attack in enumerate(pokemon_a.attacks):
        print(f"{i + 1}. {attack.name}")
    user = int(input("Choose an attack: ")) - 1
    damage_d = pokemon_d.receive_damage(pokemon_a.attacks[user])
    cpu_attack = random.choice(pokemon_d.attacks)
    damage_a = pokemon_a.receive_damage(cpu_attack)
    print(f"{pokemon_d.name} recibió {damage_d} de daño!")
    print(f"Tu rival eligió {cpu_attack}")
    print(f"{pokemon_a.name} recibió {damage_a} de daño!")
    if pokemon_d.is_alive == False:
        print(f"{pokemon_d.name} murió")
    if pokemon_a.is_alive == False:
        print(f"{pokemon_a.name} murió")
