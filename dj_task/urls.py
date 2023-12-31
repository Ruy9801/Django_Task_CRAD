"""
URL configuration for dj_task project.

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
from dj_app.views import posts_list, posts_list_api_view, post_details_api_view, create_post_api_view, delete_post_api_view, update_post_api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listing/', posts_list),
    path('api/listing/', posts_list_api_view),
    path('api/details/<int:id>/', post_details_api_view),
    path('api/create/', create_post_api_view),
    path('api/delete/<int:id>/', delete_post_api_view),
    path('api/update/<int:id>/', update_post_api_view)
]
