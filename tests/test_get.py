# Segundo test que consume una api por intermedio de GET
import os
import pytest
import requests

def test_get():

    # Obtengo la variable global que tiene el id de la persona dada de alt
    nro_persona = os.environ.get('ID_Test')
# Obtengo la api y envio el id de la persona
    respuesta_get = requests.get(
        f"http://cursotesting.com.ar:3000/consultapersona/{nro_persona}")
    
    print(respuesta_get)

    respuesta_datos = respuesta_get.json()

    print(respuesta_datos)
# aserciones del test:
    assert respuesta_datos["nombre"] == "Nombre usuario2"
    assert respuesta_datos["apellido"] == "Apellido usuario2"

if __name__ == "__main__":
    pytest.main(["-s", __file__])
