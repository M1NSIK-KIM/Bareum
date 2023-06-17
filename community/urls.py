from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('list/', views.PostListView.as_view(), name='post-list'),
    path('write',views.write_post)
]
