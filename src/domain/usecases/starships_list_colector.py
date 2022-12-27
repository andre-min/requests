from abc import ABC, abstractclassmethod
from typing import Dict, List

class StarshipsListColectorInterface(ABC):
    ''' Starships colector interface '''

    @abstractclassmethod
    def list(self, page: int) -> List[Dict]:
        ''' Must implement '''

        raise Exception('Must implement list method')