"""
URL configuration for drfproject project.

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
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from movies.views import CategoryViewSet, MovieList, MovieUpdate, MovieDestroy

# movies_router = DefaultRouter()
# movies_router.register(r'movies', MovieViewSet)
# movies_router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movies/', MovieList.as_view()),
    path('api/v1/movies/<int:pk>/', MovieUpdate.as_view()),
    path('api/v1/movies_delete/<int:pk>/', MovieDestroy.as_view()),
]
