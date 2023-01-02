from .starships_list_colector import StarshipsListColector
from src.infra import SwapiApiConsumer
#from src.infra.test.swapi_api_consumer import SwapiApiConsumerSpay #Mock

def test_list():
    ''' Testing list method '''
    #api_consumer = SwapiApiConsumerSpay()#Mock
    api_consumer = SwapiApiConsumer()

    starships_list_colector = StarshipsListColector(api_consumer)

    page = 1
    response = starships_list_colector.list(page)

    #assert api_consumer.get_starships_attributes == {"page": page}#Apenas para mock
    assert isinstance (response, list)
    assert "id" in response[0]
    assert "MGLT" in response[0]

    print()
    print(response)