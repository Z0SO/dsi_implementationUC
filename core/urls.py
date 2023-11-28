"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from productos import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('log-in', views.log_in, name='log-in'),
    path('', views.log_in, name='log-in'),
    #path('sign-up/', views.sign_up , name='sign-up'),
    path('productos/', views.productos, name='productos'),
    path('log-out/', views.sign_out, name='log-out'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('producto_nuevo/', views.crear_producto, name='nuevo_producto'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('producto/<int:prod_id>/', views.detalle_prod, name='detalle_prod'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)