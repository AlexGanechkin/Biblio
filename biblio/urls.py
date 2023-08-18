
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from biblio import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('books.urls')),
    path('reader/', include('readers.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
