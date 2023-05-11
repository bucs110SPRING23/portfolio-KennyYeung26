import requests
import random

class FruitAPI:

    def __init__(self):
        """
        Instantiates the fruit API object and gets a list of information related to all fruits
        args: none
        return: none
        """
        self.url = f'https://www.fruityvice.com/api/fruit/all'
        r = requests.get(self.url)
        self.response = r.json()

    def get(self):
        """
        This method creates generates a random fruit from the list and removes fruit that were already chosen.
        It saves the fruit name and their sugar level as a instance variable.
        args: none
        return: none
        """
        fruit = random.choice(self.response)
        self.response.remove(fruit)
        self.fruit_name = fruit["name"]
        self.sugar_level = fruit["nutritions"]["sugar"]
        return (fruit)

    def __str__(self):
        """
        Returns the string representation of the object as a number associated with the name of the pokemon
        args: none
        return: (str) the string representation of the object as a number associated with the name of the pokemon
        """
        return ("The sugar level in " + self.fruit_name + " is " + str(self.sugar_level) + ".")