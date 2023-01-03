from fastapi import Request as RequestFastApi
from typing import Callable

async def request_adapters(request: RequestFastApi, callback: callable):
    ''' FastApi adapters '''

    body = None

    try:
        body = await request.json()
    except:
        pass
    
    http_request = {
        'query_params': request.query_params,
        'body': body
    }

    try:
        http_response = callback(http_request)
        return http_response
    except:
        print('An Error Has Occurred')
    