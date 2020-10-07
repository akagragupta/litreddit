from django.urls import path,include
from pullpost import views
urlpatterns = [
    path('',views.home),
    # path('accesstoken/', views.accesstoken),
]