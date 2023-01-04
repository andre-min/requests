from src.infra.swapi_api_consumer import SwapiApiConsumer
from src.data.usescases.starship_information_colector import StarshipsInformationColector
from src.presenters.controllers.starship_information_colector_controller import StarshipInformationColectorController

def get_starships_information_composer():
    ''' Composer '''
    infra = SwapiApiConsumer()
    usecase = StarshipsInformationColector(infra)
    controller = StarshipInformationColectorController(usecase)

    return controller