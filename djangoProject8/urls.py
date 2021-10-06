"""djangoProject8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

import login_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_app.views.LoginView.as_view()),
    path('pagina/',login_app.views.vista_ejemplo),
    path('listado/',login_app.views.vista_listado),
    path('listado/<int:numpagina>/',login_app.views.vista_listado)
]

