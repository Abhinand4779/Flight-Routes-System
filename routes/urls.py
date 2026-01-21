from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_route, name='add_route'),
    path('nth-node/', views.find_nth_node, name='find_nth_node'),
    path('shortest-route/', views.shortest_route_between, name='shortest_route_between'),
    path('longest-route/', views.longest_route, name='longest_route'),
]
