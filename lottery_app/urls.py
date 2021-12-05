from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('details/<int:category_id>/',views.details,name='details'),
    path('add_details/<int:category_id>/',views.add_details,name='add_details'),
    path('search', views.searching, name='search')




]