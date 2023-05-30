import pytest
import requests

def test_get():
    #consumiendo api
    response_get = requests.get('http://cursotesting.com.ar:3000/consultapersona/13626')
    # url + nro puerto + endpoint + parametro

    print(response_get)
    response_data = response_get.json()
    print(response_data)

if __name__ == "__main__":
    pytest.main([__file__])    
