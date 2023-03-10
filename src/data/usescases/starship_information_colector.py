from src.domain.usecases.starship_information_colector import StarshipInformationColectorInterface
from src.data.interfaces.swapi_api_consumer import SwapiApiConsumerInterface
from typing import Type, Dict
from src.errors import HttpUnprocessableEntityError


class StarshipsInformationColector(StarshipInformationColectorInterface):
    ''' StarshipsInformationColector usecase '''

    def __init__(self, api_consumer: Type[SwapiApiConsumerInterface]) -> None:
        self.__api_consumer = api_consumer

    def find_starships(self, starships_id: int, time: str) -> Dict:
        ''' 
            Find starship information and return it 
            :param - starship_id: Id of the starship
                    - time: Time in hours
            :returns - Dictionary with satarship information        
        '''
        starship_information = self.__search_starships(starships_id)
        mglt = starship_information['MGLT']

        distance_traveld = self.__calculate_distance_traveled_to_spaceship(mglt, time)
        
        formated_response = self.__format_response(starship_information, distance_traveld)
        return formated_response

    def __search_starships(self, starships_id: int):
        '''
            Get Starship and validade information 
            :param - starship_id: Id of the starship
            :returns - Dictionary with starship information from API
        '''

        api_response = self.__api_consumer.get_starship_information(starships_id)
        if api_response.response['MGLT'] == 'unknown':
            raise HttpUnprocessableEntityError('Unprocessible Information for selected starship')

        return api_response.response
        
    @classmethod
    def __calculate_distance_traveled_to_spaceship(cls, mglt: str, time: str) -> int:
        '''
            Algorithm to calcule distance traveled
            :param - mglt: string with Maximum number of Megalights for this spaceship
                   - Time: Time in hours 
            :returns - distace traveled in megalights
        '''

        distance_traveled = int(mglt) * int(time)
        return distance_traveled

    @classmethod
    def __format_response(cls, starship_information: Dict, distance_traveled: int) -> Dict:
        return {
            "name": starship_information["name"],
            "model": starship_information["model"],
            "manufacturer": starship_information["manufacturer"],
            "max_atmosphering_speed": starship_information["max_atmosphering_speed"],
            "MGLT": starship_information["MGLT"],
            "distance_traveled": str(distance_traveled) + " ML"
        }

        