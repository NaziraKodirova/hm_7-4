from django.urls import path, include
from .views import ArtistAPIView, ArtistDetailAPIView, AlbomDetailAPIView, AlbomAPIView, SongsAPIViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('songs', viewset=SongsAPIViewSet)

urlpatterns = [
    path('artists/', ArtistAPIView.as_view(), name='artists'),
    path('artists/<int:id>', ArtistDetailAPIView.as_view(), name='artist-detail'),
    path('alboms/', AlbomAPIView.as_view(), name='alboms'),
    path('alboms/<int:id>', AlbomDetailAPIView.as_view(), name='albom-detail'),
    path('', include(router.urls)),
]
