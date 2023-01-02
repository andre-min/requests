from src.domain.usecases import StarshipsListColectorInterface
from typing import Dict, List, Type
from src.data.interfaces.swapi_api_consumer import SwapiApiConsumerInterface


class StarshipsListColector(StarshipsListColectorInterface):
    ''' StarshipsListColector use case '''

    def __init__(self, api_consumer: Type[SwapiApiConsumerInterface]) -> None:
        self.__api_consumer = api_consumer
        
    def list(self, page: int) -> List[Dict]:
        api_response = self.__api_consumer.get_starships(page)
        starships_formated_list = self.__format_api_response(api_response.response["results"])
        return starships_formated_list

    @classmethod
    def __format_api_response(cls, results: List[Dict]):
        starships_formated_list = []

        for starships in results:
            starships_formated_list.append(
                {
                    "id": starships["url"].split("/")[-2],
                    "name": starships["name"],
                    "model": starships["model"],
                    "max_atmosphering_speed": starships["max_atmosphering_speed"],
                    "hyperdrive_rating": starships["hyperdrive_rating"],
                    "MGLT": starships["MGLT"],

                }
            )
        return starships_formated_list

