from abc import ABC, abstractclassmethod
from typing import Dict

class StarshipInformationColectorInterface(ABC):
    ''' Starship Information Colector Interface '''

    @abstractclassmethod
    def find_starships(self, starships_id: int, time: str) -> Dict:
        ''' Must implement '''

        raise Exception('Must implement find_starships method')