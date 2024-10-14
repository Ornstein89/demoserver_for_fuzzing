"""
URL configuration for rest_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken.views import ObtainAuthToken
from mainapp.views import BookView
# from .views import NodeDocTreeView, NodeView, DocumentView, VersionView, LogView, SearchQueryView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', ObtainAuthToken.as_view()),
    
    path('api/book/list',   BookView.as_view({'post' : 'list'})),
    path('api/book/get',    BookView.as_view({'post' : 'retrieve'})),
    path('api/book/update', BookView.as_view({'post': 'update'})),
    # path('api/book/create', BookView.as_view({'post': 'create'})), # заглушено во избежание изменения размеров БД
    # path('api/book/delete', BookView.as_view({'get' : 'delete'})), # заглушено во избежание изменения размеров БД
]
