# Sansamarket

Aplicación web de publicaciones de productos desarrollada con Python y Django. Permite gestionar anuncios, consultar perfiles de vendedores y registrar reseñas entre usuarios.

## Funcionalidades presentes en el código

- Registro, inicio y cierre de sesión.
- Perfiles con avatar, biografía y datos de contacto.
- Listado y detalle de productos con precio e imagen.
- Creación, edición y eliminación de publicaciones, con comprobación del propietario.
- Reseñas de usuarios con puntuaciones de 1 a 5 y visualización del promedio.

## Tecnologías y estructura

Python · Django 5.1.1 · SQLite · HTML/CSS · Plantillas Django.

- `Proyecto/Apps/`: usuarios, productos, reseñas y módulo inicial de favoritos.
- `Proyecto/Apps/templates/`: interfaz.
- `Proyecto/Proyecto/`: configuración y rutas.
- `Proyecto/manage.py`: administración del proyecto.
- `requirements.txt`: dependencias declaradas.

## Preparación local

Crear un entorno virtual nuevo e instalar las dependencias de `requirements.txt`. Revisar además Pillow, necesario para los campos de imagen. Desde `Proyecto/`, aplicar las migraciones con `python manage.py migrate` e iniciar el servidor con `python manage.py runserver`.

Estas instrucciones requieren validación en un entorno limpio.

## Estado y pendientes

Código orientado a desarrollo local. Favoritos está pendiente de implementación. No se incluyen flujos de carrito, pedidos ni pagos. Quedan por validar los recorridos completos, completar pruebas automatizadas y corregir detalles de autenticación y exploración de productos.
