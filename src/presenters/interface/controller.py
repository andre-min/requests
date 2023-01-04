from typing import Dict
from abc import ABC, abstractmethod

class ControllerInterface(ABC):
    ''' Interface to Controle '''

    @abstractmethod
    def handler(self, http_request: Dict):
        ''' Method to handle request '''
        raise 'Should implement handler method'