from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('StudioPublish', views.StudioPublish, name="StudioPublish"),
    path('RegionConsole', views.RegionConsole, name="RegionConsole"),
    path('Contributor', views.Contributorview, name="Contributor")
]