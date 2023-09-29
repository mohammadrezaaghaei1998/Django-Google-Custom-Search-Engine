from django.urls import path
from .import views


urlpatterns = [

    path('',views.search_view,name='search_view'),
    path('',views.second_search_view,name='second_search_view'),
]
