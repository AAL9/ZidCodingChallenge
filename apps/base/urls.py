from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = "Home"),
    path('CreateWaybill', views.CreateWaybill, name = "CreateWaybill"),
    path('PrintWaybill', views.PrintWaybill, name = "PrintWaybill"),
    path('TrackShipment', views.TrackShipment, name = "TrackShipment"),
    path('CancelWaybill', views.CancelWaybill, name = "CancelWaybill"),
]