# Proyecto Urban Grocers 

Este proyecto tiene como objetivo la creación de pruebas
automatizadas para la funcionalidad de la creación de los 
9 kits de productos en la aplicación Urban Grocers.
La función principal de estas pruebas es verificar el campo "name" en la creación de los kits.

# Archivos en el Proyecto

- 'configuration.py' - Configuración de las URLs del servidor
    La URL_SERIVE se debe actualizar cada cierto tiempo, de lo contrario el programa no correrá.
- 'data.py' - Cuerpos de solicitud (JSON)
- 'sender_stand_request.py' - Funciones que envian las solicitudes HTTP
- 'create_kit_name_kit_test.py' - Casos de Prueba automatizados
- 'README.md' - Documentación específica del proyecto
- '.gitignore' - Archivos que se ignorar por Git


# Pasos para ejecutar las pruebas automatizadas
1. Instalar las bibliotecas necesarias
    requests, pytest
2. Iniciar el servidor de Urban Grocers
3. Actualizar la URL del servidor en el archivo 'configuration.py' en el campo URL_SERVICE
4. Asegurarse que la ejecución de las pruebas se realice con pytest:
    pytest create_kit_name_kit_test.py
