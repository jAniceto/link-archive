from django.urls import path
from mox_api import views


urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('links/', views.link_list, name='link-list'),
    path('links/<int:pk>/', views.link, name='link'),
]