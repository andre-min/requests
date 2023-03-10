from abc import ABC, abstractclassmethod
from requests import Request
from typing import Type, Dict, Tuple

class SwapiApiConsumerInterface(ABC):
    ''' Api consumer interface '''

    @abstractclassmethod
    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        ''' Must Implement '''
        raise Exception('Must implement get_starships')

    @abstractclassmethod
    def get_starship_information(self, starship_id: int) -> Tuple[int, Type[Request], Dict]:
        ''' Must Implement '''
        raise Exception('Must implement get_starship_information')
