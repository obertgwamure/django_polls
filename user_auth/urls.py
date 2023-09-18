from django.urls import path, include
from .import views

# URL Patterns
app_name = 'user_auth'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user,name='authenticate_user'),
    path('shower_user/', views.show_user,name='show_user'),
    path('user_registration/', views.user_registration, name='registration')
]
