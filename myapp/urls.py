# urls.py in your Django app directory

from django.urls import path
from .views import questionnaire,scores,intro

urlpatterns = [
    path('', intro, name='intro'),
    path('questionnaire/', questionnaire, name='questionnaire'),
    path('scores/<int:total_score>/<str:user_name>/', scores, name='scores'),
]
