"""StudyPoint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from .views import about, index, contactus
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index),
    path('about/', about),
    path('contact/', contactus),
    path('admin/', admin.site.urls),
    path('firstyear/', include('Firstyear.urls')),
    path('ECE/', include('ECE.urls')),
    path('CSE/', include('CSE.urls')),
    path('CHE/', include('CHE.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
