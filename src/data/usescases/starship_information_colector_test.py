from src.data.usescases.starship_information_colector import StarshipsInformationColector
from src.infra.test.swapi_api_consumer import SwapiApiConsumerSpay 

def test_find_starship():
    ''' Testing find_starship method '''

    api_consumer = SwapiApiConsumerSpay()
    starship_information_colector = StarshipsInformationColector(api_consumer)
    starship_id = 9
    time = 4
    response = starship_information_colector.find_starships(starship_id, time)
   
    assert api_consumer.get_starship_information_attributes['starship_id'] == starship_id
    assert isinstance(response, dict)
    assert 'MGLT' in response
    assert 'distance_traveled' in response
