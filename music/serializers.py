from rest_framework import serializers
from .models import Artist, Albom, Songs


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("id", 'name', 'image', 'last_updated')


class AlbomSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Albom
        fields = ("id", 'title', 'artist', 'cover', 'last_updated')


class SongsSerializer(serializers.ModelSerializer):
    albom = AlbomSerializer(read_only=True)

    class Meta:
        model = Songs
        fields = ("id", 'title', 'cover', 'albom', 'last_updated')


