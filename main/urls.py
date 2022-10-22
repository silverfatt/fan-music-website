from django.conf.urls.static import static
from django.urls import path

from sabaton import settings
from .views import MainPage, PatricipantsList, AlbumDetail, ParticipantDetail, AboutView, PhotoDetail, AlbumsList, \
    PhotoList
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
                  path('', MainPage.as_view(), name='main_page'),
                  path('participants/', PatricipantsList.as_view(), name='participants'),
                  path('participants/<int:pk>/', ParticipantDetail.as_view(), name='participant'),
                  path('albums/', AlbumsList.as_view(), name='albums'),
                  path('albums/<int:pk>/', AlbumDetail.as_view(), name='album'),
                  path('gallery/', PhotoList.as_view(), name='gallery'),
                  path('about/', AboutView.as_view(), name='about'),
                  path('gallery/<int:pk>', PhotoDetail.as_view(), name='photo'),
                  path('login/', LoginView.as_view(), name='login'),
                  path('logout/', LogoutView.as_view(), name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
