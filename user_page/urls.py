from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_page, name='user_page'),
    path('refresh/', views.refresh_user_info, name='refresh_user_info'),
    path('auth/', views.auth_page, name='auth_page'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('edit/', views.edit_user_info, name='edit_user_info'),
    path('save/', views.save_user_info, name='save_user_info'),
]