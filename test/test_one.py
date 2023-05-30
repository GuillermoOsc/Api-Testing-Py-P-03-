import pytest
import requests

def test_get():
    nro_user = 13628
    #consumiendo api
    response_get = requests.get(f"http://cursotesting.com.ar:3000/consultapersona/{nro_user}")
    # url + nro puerto + endpoint + parametro

    print(response_get)
    response_data = response_get.json()
    print(response_data)

if __name__ == "__main__":
    pytest.main(["-s",__file__])    
