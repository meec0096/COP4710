from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('console', views.insertConsole, name="insertConsole"),
    path('contributor', views.insertContributor, name ="insertContributor"),
    path('region', views.insertRegion, name ="Region"),
    path('studio', views.insertStudio, name = "Studio"),
    path('publisher', views.insertPublisher, name = 'Publisher'),
    path('game', views.insertGame, name ="Game"),
]