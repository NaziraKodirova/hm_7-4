from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Albom, Songs
from .serializers import ArtistSerializer, AlbomSerializer, SongsSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet


class ArtistAPIView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        try:
            serializer = ArtistSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ArtistDetailAPIView(APIView):
    def get(self, request, id):
        try:
            artists = Artist.objects.get(id=id)
            serializer = ArtistSerializer(artists)
            return Response(data=serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        artists = Artist.objects.get(id=id)
        serializer = ArtistSerializer(instance=artists, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        artists = Artist.objects.get(id=id)
        serializer = ArtistSerializer(instance=artists, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        artists = Artist.objects.get(id=id)
        artists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlbomAPIView(APIView):
    def get(self, request):
        albums = Albom.objects.all()
        serializer = AlbomSerializer(albums, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        try:
            serializer = AlbomSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AlbomDetailAPIView(APIView):
    def get(self, request, id):
        try:
            albom = Albom.objects.get(id=id)
            serializer = AlbomSerializer(albom)
            return Response(data=serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        albom = Albom.objects.get(id=id)
        serializer = AlbomSerializer(instance=albom, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        albom = Albom.objects.get(id=id)
        serializer = AlbomSerializer(instance=albom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        albom = Albom.objects.get(id=id)
        albom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SongsAPIViewSet(ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
