from .api import index_content
from .views import index_view
from django.urls import path


urlpatterns = [
    path('', index_view),
    path('api_index_content', index_content),
]