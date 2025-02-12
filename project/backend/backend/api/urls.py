from . import views
from django.urls import path

urlpatterns = [
    path('get_visualnovel/', views.get_visualnovel),
    path('search_visualnovel/', views.search_visualnovel),
    path('get_visualnovels_by_genre/', views.get_visualnovels_by_genre),
    path('create_visual_novel/', views.create_visual_novel),
    path('get_user_info/', views.get_user_info),
]
