from django.urls import path

from . import views
urlpatterns=[
    path('',views.home,name="home page"),
    path('game1/',views.game1,name='page_game1'),
]