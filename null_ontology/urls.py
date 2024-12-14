from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='__main'),
    path('<str:category>/', views.browse, name='browse'),
    path('<str:category>/<slug:post_slug>/', views.content, name='content'),
]
