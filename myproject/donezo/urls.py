from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view/', views.landing_page, name='landing_page'),  # existing home view
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]