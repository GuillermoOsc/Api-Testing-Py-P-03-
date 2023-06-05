import os
import pytest
import requests

def test_get():

    nro_persona = os.environ.get('ID_Test')

    respuesta_get = requests.get(
        f"http://cursotesting.com.ar:3000/consultapersona/{nro_persona}")

    print(respuesta_get)

    respuesta_datos = respuesta_get.json()
# convertida la respuesta a json puedo acceder a los datos reales que me envía
    print(respuesta_datos)
# aserciones del test:
    assert respuesta_datos["nombre"] == "María"
    assert respuesta_datos["apellido"] == "Perez"

if __name__ == "__main__":
    pytest.main(["-s", __file__])
