from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.http import HttpResponse

def simple_home(request):
    return HttpResponse("""
    <h1>API de Productos</h1>
    <p>API REST con Django DRF desplegada en Render</p>
    <ul>
        <li><a href="/api/productos/">/api/productos/</a> - API Productos</li>
        <li><a href="/admin/">/admin/</a> - Panel Admin</li>
    </ul>
    """)

urlpatterns = [
    path('', simple_home, name='home'),
    path('admin/', admin.site.urls),
    path('', include('productos.urls')),
]