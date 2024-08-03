from django.urls import path
from .views import TitleList, PersonList

urlpatterns = [
    path('titles/', TitleList.as_view(), name='title-list'),
    path('persons/', PersonList.as_view(), name='person-list'),
]
