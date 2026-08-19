from django.urls import path

from . import views
urlpatterns = [
    path('', views.game2, name='page_game2')
]
