# Primer test que consume una api por intermedio de post

import os
import pytest
import requests

#Definición de la función: 
def test_post():
#consumiento la api 
# url + nro de puerto + endpoint + parámetro

    api_nueva = "http://cursotesting.com.ar:3000/nuevapersona/"

# armado del conjunto de datos que contiene los valores a enviar para generar la nueva persona
# se guarda en la variable “datos” y las llaves y las comas es para representarlo en formato json
    datos = {       
        "nombre" : "Nombre usuario2",
        "apellido" : "Apellido usuario2",
        "edad" : 30
    }

#consumiento la api 
# envío la url y separado por una coma el conjunto de datos

    respuesta_post = requests.post(api_nueva, json=datos)

# muestro el código de respuesta de la api
    print(respuesta_post)


# convierto la respuesta en formato json.
# convertida la respuesta a json puedo acceder a los datos reales que me envía
    respuesta_datos = respuesta_post.json()

    print(respuesta_datos)
    

#aserciones del test:

    assert respuesta_post.status_code == 200,f"Código devuelto: {respuesta_post.status_code}"

# chequeo que dentro del json devuelto se incluya un campo “id”
    assert "id" in respuesta_datos, "Error no devolvió el id"

# también analizo la respuesta en forma lógica para poder tomar acciones
    if respuesta_post.status_code == 200:
        print("Ingreso Correcto")

# si devuelve un código 200  creo una variable global
        os.environ['ID_Test'] = str(respuesta_datos["id"]) # convierto en string ( alfanumerico )

# hago otra aserción. Chequeo que el código “id” de las personas tienen que ser mayores a 130.000
        assert respuesta_datos["id"] > 130000
    else:
        print("Cuidado, código de error!")

# llamo al test para que se autoejecute con la extensión de Python de Visual Studio Code
if __name__ == "__main__":
    pytest.main(["-s",__file__])

