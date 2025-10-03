from sender_stand_request import get_new_user_token, post_new_client_kit
from data import kit_body_1, kit_body_2, kit_body_3,kit_body_4, kit_body_5, kit_body_6, kit_body_7, kit_body_8,kit_body_9


# Función que contiene la lógica común de pruebas positivas
def positive_assert(kit_body):
    # Llama a la función
    auth_token = get_new_user_token()

    # Llamar a la función pasando dos parámetros
    kit_response = post_new_client_kit(kit_body, auth_token)

    # Primera verificación - comprueba que el código de verifiación sea 201
    assert kit_response.status_code == 201

    # Segunda verificación
    # Convierte la respuesta en JSON
    # Compara el campo name que enviaste a kit_body_1
    assert kit_response.json()["name"] == kit_body["name"]


#Funcion que contiene logica comun de pruebas negativas
def negative_assert_code_400(kit_body):
    # Llama a la función
    auth_token = get_new_user_token()

    # Llamar a la función pasando dos parámetros
    kit_response = post_new_client_kit(kit_body, auth_token)

    # Primera verificación - comprueba que el código de verifiación sea 201
    assert kit_response.status_code == 400

#Función de Prueba 1
def test_create_kit_1_character():
    positive_assert(kit_body_1)

#Función de Prueba 2
def test_create_kit_511_character():
    positive_assert(kit_body_2)

#Función de Prueba 3
def test_create_kit_0_character():
    negative_assert_code_400(kit_body_3)

#Función de Prueba 4
def test_create_kit_512_character():
    positive_assert(kit_body_4)

#Función de Prueba 5
def test_create_kit_special_character():
    positive_assert(kit_body_5)

#Función de Prueba 6
def test_create_kit_spaces():
    positive_assert(kit_body_6)

#Función de Prueba 7
def test_create_kit_numbers():
    positive_assert(kit_body_7)

#Función de Prueba 8
def test_create_kit_no_character():
    negative_assert_code_400(kit_body_8)

#Función de Prueba 9
def test_create_kit_different_character():
    negative_assert_code_400(kit_body_9)
