from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('home/',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('faqs/',views.faqs),
    path('jobs/',views.jobs),
    path('login/',views.login),
    path('news/',views.news),
    path('videonews/',views.videonews),
    path('newsdetails/',views.newsdetails),
    path('portfolio/',views.portfolio),
]