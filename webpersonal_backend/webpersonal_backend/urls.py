"""
URL configuration for webpersonal_backend project.

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
from core import views as coreviews #Se importa views para mostrar las listas por medio de las urls en este archivo
from portfolio import views as portfolioviews
from django.conf import settings

urlpatterns = [
    path('', coreviews.home, name="home"), 
    path('about-me/', coreviews.about, name="about"), #Llamado de vista home para renderizar funcion home del views.py
    path('portfolio/', portfolioviews.portfolio, name="portfolio"), 
    path('contact/', coreviews.contact, name="contact"), 
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #MOSTRAR ARCHIVOS EN SERVIDOR DEBUG, recuerda media_url y media_root se declaran en setting.py