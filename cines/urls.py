from . import views
from django.urls import include, path

urlpatterns = [
    path('Cine/', views.cineListView.as_view(), name='Cine_list'),
    path('Cine/add', views.cineCreateView.as_view(), name='Cine_add'),
    path('Cine/<int:pk>/edit', views.   cineUpdateView.as_view(), name='Cine_update'),
     path('Cine/<int:pk>/delet', views.   cineDeleteView.as_view(), name='Cine_delete'),
]