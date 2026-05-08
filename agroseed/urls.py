# agroseed/urls.py
from django.urls import path, include

urlpatterns = [
    path('api/', include('core.urls')),
]

from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
]