from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.start, name='album-start'),
    path('home/', views.home, name='album-home'),
    path('album/', views.album, name='album'),
    path('invertebrate/<int:pk>', views.invertebrate, name='invertebrate-info'),
    path('add/', views.add_invertebrate, name='add-invertebrate'),
    path('invertebrate/<int:pk>/delete/', views.delete_invertebrate, name='delete-invertebrate')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)