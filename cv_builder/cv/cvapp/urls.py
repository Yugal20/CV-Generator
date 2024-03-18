from django.urls import path
from cvapp import views

urlpatterns=[
    path('',views.index),
    path('<int:id>/',views.resume),
    path('list',views.list),
    path('download',views.download)
]