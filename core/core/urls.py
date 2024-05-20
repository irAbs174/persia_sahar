"""
BASE URL SETTINGS => {
    FOR WGSI APPLICATION,
    DEVELOPER : #ABS
}
"""

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
import os


# BASE URL PATTERNS
urlpatterns = [
    path('unique/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))