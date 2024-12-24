from django.urls import path
from . import views

urlpatterns = [
    path("", views.markets_home_view, name="markets-home-view"),
    path("search-stocks/", views.search_stocks, name="search-stocks"),
]
