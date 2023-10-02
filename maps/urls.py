"""
URL configuration for maps project.

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

from village import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.IndexView.as_view(), name="index"),
    path('create/', views.VillageCreateView.as_view(), name='village_create'),  
    path("list_view/", views.VillageListView.as_view(), name="village_list_view"),
    path("<int:pk>/delete/", views.VillageDeleteView.as_view(), name="village_delete"),
    path("<int:pk>/update/", views.VillageUpdateView.as_view(), name="village_update"),
    path('<int:pk>/detail/', views.VillageDetailView.as_view(), name='village_detail'),

    ]

