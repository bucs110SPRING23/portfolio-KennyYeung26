import requests

class FruitAPI:

    def __init__(self):
        """
        Instantiates the fruit API object
        args: none
        return: none
        """
        self.url = f'https://www.fruityvice.com/api/fruit/all'

    def get(self):
        """
        gets a dictionary of the list of information related to all fruits
        args: none
        return: none
        """
        r = requests.get(self.url)
        response = r.json()
        return (response)