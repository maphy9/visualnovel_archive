from . import views
from django.urls import path

urlpatterns = [
    path('get_visualnovel/', views.get_visualnovel),
    path('get_visualnovels_by_genre/', views.get_visualnovels_by_genre),
    path('get_visualnovels_by_developer/', views.get_visualnovels_by_developer),
    path('get_visualnovels_by_publisher/', views.get_visualnovels_by_publisher),

    path('get_user_by_username/', views.get_user_by_username),

    path('search_visualnovel/', views.search_visualnovel),
    path('search_genre/', views.search_genre),
    path('search_developer/', views.search_developer),
    path('search_publisher/', views.search_publisher),
    
    path('create_visualnovel/', views.create_visualnovel),
    path('create_genre/', views.create_genre),
    path('create_developer/', views.create_developer),
    path('create_publisher/', views.create_publisher),
]
