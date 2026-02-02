from django.urls import path
from .views import start_page, save_content

urlpatterns = [
    path('', start_page, name='home'),
    path('save/', save_content, name='save_content'),
]