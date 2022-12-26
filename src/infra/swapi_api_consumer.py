import requests

class SwapiApiConsumer():
    @classmethod
    def get_starships(self, page: int) -> any:
        params = {'page': page}
        response = requests.get('http://swapi.dev/api/starships/', params=params)

        return response.json()