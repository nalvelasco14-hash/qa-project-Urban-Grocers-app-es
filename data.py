headers = {
    "Content-Type": "application/json"
   }

user_body = {
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

#Número permitido de carácteres (1)
kit_body_1 = {
    "name": "a"
}

#Número permitido de carácteres (511)
kit_body_2 = {
    "name": "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabC"
}

#Número permitido de carácteres (0)
kit_body_3 = {
    "name": ""
}

#Número permitido de carácteres (512)
kit_body_4 = {
    "name": "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcD"
}

#Carácteres especiales permitidos
kit_body_5 = {
    "name": "'N°@%"
}

#Se permiten espacios
kit_body_6 = {
    "name": " A Aaa "
}

#Se permiten números
kit_body_7 = {
    "name": "123"
}

#El parámetro no se pasa en la solicitud
kit_body_8 = {

}

#Se ha pasado un tipo de parámetro diferente (Número)
kit_body_9 = {
    "name": 123
}