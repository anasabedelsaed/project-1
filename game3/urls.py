from django.urls import path

from . import views
urlpatterns=[
    path('',views.game3,name='page_game3'), # type: ignore
    
]