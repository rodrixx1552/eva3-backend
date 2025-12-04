# API REST de Productos con Django DRF

API REST desarrollada con Django REST Framework, desplegada en Render.

## Endpoints
- `GET /api/productos/` - Listar productos
- `POST /api/productos/` - Crear producto
- `GET /api/productos/{id}/` - Obtener producto
- `PUT /api/productos/{id}/` - Actualizar producto
- `PATCH /api/productos/{id}/` - Actualizar parcial
- `DELETE /api/productos/{id}/` - Eliminar producto

## Despliegue
API disponible en: [URL_RENDER]

## Tecnologías
- Django 5.2.9
- Django REST Framework
- PostgreSQL (Render)
- WhiteNoise (archivos estáticos)
- Gunicorn (servidor WSGI)