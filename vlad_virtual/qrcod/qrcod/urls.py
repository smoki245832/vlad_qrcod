from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home_page'),
    path('news/', include('news.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
