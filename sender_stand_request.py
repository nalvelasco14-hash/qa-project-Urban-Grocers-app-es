import configuration
import requests #Biblioteca de python para hacer llamadas a HTTP
import data

#Función para la creación de un nuevo usuario
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=user_body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

#Función para la creación de un nuevo kit
def post_new_client_kit(kit_body, auth_token):
    # Necesitas crear headers que incluyan el token
    headers = data.headers.copy()  # Copia los headers originales
    headers["Authorization"] = f"Bearer {auth_token}"  # Agrega el token

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, # inserta la dirección URL completa
                         json=kit_body, # inserta el cuerpo de solicitud
                         headers=headers) # inserta los encabezados

#Función para obtener el authToken
def get_new_user_token():
    # Crear un nuevo usuario
    user_response = post_new_user(data.user_body)
    # Extraer el token de la respuesta
    return user_response.json()["authToken"]
