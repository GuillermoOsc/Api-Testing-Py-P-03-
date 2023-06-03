# Tercer test que consume una api por intermedio de la acción PUT
import os
import pytest
import requests
 
def test_put():
# Obtengo la variable global que tiene el id de la persona dada de alta 
# esta variable la creo en el archivo test_nueva.py

    nro_usuario = os.environ.get('ID_Test')

# url + nro de puerto + endpoint + parámetro 
# Se indica el nro de id para que la api modifique el usuario
    api_modifica = f"http://cursotesting.com.ar:3000/cambiar/{nro_usuario}"

    datos = {       
        "nombre" : "María",
        "apellido" : "Gomez"
    }

#consumiento la api 
    respuesta_put = requests.put(api_modifica, json=datos)

# Se muestra el código de respuesta. La api, en este caso, no devuelve más datos
    print(respuesta_put)

# Se llama al test para que se autoejecute con la extensión de Python de Visual Studio Code
if __name__ == "__main__":
    pytest.main(["-s",__file__])


