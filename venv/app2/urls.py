from django.urls import path
from app2.views import index, url2, url3

urlpatterns = [
    path('', index),
    path('url2/', url2),
    path('url3/', url3)
]