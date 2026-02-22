from django.urls import path
from .views import start_page, save_content, check_text, rephrase_text, search_history

urlpatterns = [
    path('', start_page, name='home'),
    path('check/', check_text, name='check_text'),
    path('rephrase/', rephrase_text, name='rephrase_text'),
    path('save/', save_content, name='save_content'),
    path('search/', search_history, name='search_history'),
]