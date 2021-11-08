from django.urls import path
from mox_api import views


urlpatterns = [
    # Root
    path('', views.api_root, name='api-root'),
    # Links
    path('links/', views.link_list, name='link-list'),
    path('links/<int:pk>/', views.link, name='link'),
    # Tags
    path('tags/', views.tag_list, name='tag-list'),
    path('tags/<int:pk>/', views.tag, name='tag'),
]