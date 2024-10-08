from django.http import HttpResponse

# Request: Para realizar peticiones.
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP

# Esto es una vista
def bienvenida(request): # Pasamos una request como primer argumento
    return HttpResponse("Bienvenido o bienvenida")