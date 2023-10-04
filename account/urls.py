from django.contrib.auth import views
from django.urls import path

app_name = 'account'

urlpatterns = [
    path('',views.LoginView.as_view(),name="login"),
]