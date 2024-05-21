from .views import dashboard_index_view
from .api import dashboard_content
from django.urls import path


urlpatterns = [
    path('', dashboard_index_view),
    path('api_dashboard_content', dashboard_content),
]