from . import views
from django.urls import path

urlpatterns = [
    path('get_popular_visual_novels/', views.get_popular_visual_novels),
    path('get_new_visual_novels/', views.get_new_visual_novels),
    path('get_most_liked_visual_novels/', views.get_most_liked_visual_novels),
    path('get_random_visual_novel/', views.get_random_visual_novel),
    path('get_popular_discussions/', views.get_popular_discussions),
    path('get_new_discussions/', views.get_new_discussions),
    path('get_most_replied_to_discussions/', views.get_most_replied_to_discussions),
    path('get_most_active_users/', views.get_most_active_users),
    path('find_visual_novels/', views.find_visual_novels),
    path('find_discussions/', views.find_discussions),
    path('find_users/', views.find_users),
]
