import PokeAPI
import FruitAPI
import random

def main():

    pokemon = PokeAPI.PokeAPI()
    fruit = FruitAPI.FruitAPI()   
    fruits = fruit.get()
    n = int(input("Enter the number of pokemon you wish to feed:"))
   
    for meal_plan in range(n):

        #user input number associated to pokemon
        pokemon_number = pokemon.get(int(input("Enter a number associated to a pokemon:")))
        print(str(pokemon))
        name = pokemon_number["name"]
        weight = pokemon_number["weight"]

        #each pokemon eats different fruits(no overlap)
        fruit1 = random.choice(fruits)
        sugar1 = fruit1["nutritions"]["sugar"]
        fruits.remove(fruit1)

        fruit2 = random.choice(fruits)
        sugar2 = fruit2["nutritions"]["sugar"]
        fruits.remove(fruit2)

        fruit3 = random.choice(fruits)
        sugar3 = fruit3["nutritions"]["sugar"]
        fruits.remove(fruit3)

        if weight >= 500:
            #sugar level of 3 fruits combined can't be more than 300
            if sugar1 + sugar2 + sugar3 < 300:
                print(name + " devours a " + fruit1["name"] + " for breakfast, a " + fruit2["name"] + " for lunch, and a " + fruit3["name"] + " for dinner.")
        else:
            #sugar level of 3 fruits combined can't be more than 100
            if sugar1 + sugar2 + sugar3 < 100:
                print(name + " eats a " + fruit1["name"] + " for breakfast, a " + fruit2["name"] + " for lunch, and a " + fruit3["name"] + " for dinner.")

main()
