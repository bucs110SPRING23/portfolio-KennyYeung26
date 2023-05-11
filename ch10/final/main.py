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
        
        name = pokemon_number["name"]
        weight = pokemon_number["weight"]
        print(str(pokemon))

        #each pokemon eats different fruits(no overlap)
        fruit1 = fruit.get()
        sugar1 = fruit1["nutritions"]["sugar"]
        print(str(fruit))

        fruit2 = fruit.get()
        sugar2 = fruit2["nutritions"]["sugar"]
        print(str(fruit))

        fruit3 = fruit.get()
        sugar3 = fruit3["nutritions"]["sugar"]
        print(str(fruit))

        if weight >= 500:
            #sugar level of 3 fruits combined can't be more than 40
            if sugar1 + sugar2 + sugar3 < 40:
                print(name + " devours a " + fruit1["name"] + " for breakfast, a " + fruit2["name"] + " for lunch, and a " + fruit3["name"] + " for dinner.")
        
        else:
            #sugar level of 3 fruits combined can't be more than 10
            if sugar1 + sugar2 + sugar3 < 10:
                print(name + " eats a " + fruit1["name"] + " for breakfast, a " + fruit2["name"] + " for lunch, and a " + fruit3["name"] + " for dinner.")
            else:
                print(name + " gets an upset stomach.")
main()
