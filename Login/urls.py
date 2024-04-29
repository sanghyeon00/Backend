"""capde URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Login import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('id_check/', views.id_check),
    path('sign_up/', views.RegisterView.as_view()),
    path('sign_in/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('access_token_check/', views.my_view , name='check'),
    path('position_check/', views.position_check, name = 'position'),
    path('name_check/', views.name_check)
]
