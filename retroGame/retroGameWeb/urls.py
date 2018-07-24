from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('console', views.Consoleview, name="Console"),
    path('contributor', views.Contributorview, name ="Contributor"),
    path('region', views.Regionview, name ="Region"),
    path('studio', views.Studioview, name = "Studio"),
    path('publisher', views.Publisherview, name = 'Publisher'),
    path('game', views.Gameview, name ="Game"),

    path('gamedetails', views.insertFullGame, name ="GameDetails"),
    path('SelectPublish', views.SelectPublisher, name = "selectPublish"),
    path('SelectStudio', views.SelectStudio, name = "SelectStudio"),
    path('SelectConsole', views.SelectConsole, name = "selectConsole"),
    path('SelectRegion', views.SelectRegion, name = "selectRegion"),
    path('insertPublish', views.insertPublisher, name = "insertPublisher"),
    path('insertStudio', views.insertStudio, name = "insertStudio"),
    path('insertConsole', views.insertConsole, name = "insertConsole"),
    path('insertRegion', views.insertRegion, name = "insertRegion"),
    path('insertContributor', views.insertContributor, name = "insertContributor"),
    path('insertReleaseDate', views.insertReleaseDate, name = "insertReleaseDate"),
]