from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='home'),
    path('details/<int:category_id>/',views.details,name='details'),
    path('add_details/<int:category_id>/',views.add_details,name='add_details'),
    path('search', views.searching, name='search')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
