from django.urls import path, re_path

from blog import views

urlpatterns = [
    path('hello/', views.hello),
    re_path(r'^upload/(\w+)/(\d+)/$', views.fraction_upload),
    re_path(r'^inqurie/(\d+)/(\d+)/(\w+)/$', views.fraction_inqurie),
]