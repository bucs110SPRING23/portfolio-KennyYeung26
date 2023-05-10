import requests

class PokeAPI:

    def __init__(self):
        """
        Instantiates the pokemon API object
        args: none
        return: none
        """
        self.url = f'https://pokeapi.co/api/v2/pokemon/'

    def get(self, number):
        """
        Gets a dictionary of the information of the pokemon based its ID
        args: number
        return: response
        """
        self.number = number
        r = requests.get(self.url + str(number))
        response = r.json()
        return (response)
    
    def __str__(self):
        """
        Returns the string representation of the object as a number associated with the name of the pokemon
        args: number
        return: the string representation of the object as a number associated with the name of the pokemon
        """
        return ("Number: " + str(self.number) + " is " + self.get(self.number)["name"] + ".")
