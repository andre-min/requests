from .swapi_api_consumer import SwapiApiConsumer

def test_get_starships(requests_mock):

    ''' Testing get starships method '''

    requests_mock.get('http://swapi.dev/api/starships/', status_code=200, json={'some': 'thing'})
    swapi_api_consumer = SwapiApiConsumer()

    response = swapi_api_consumer.get_starships(page=1)

    print(response)