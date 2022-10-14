from rest_framework import serializers

from genres.models import Genre
from genres.serializers import GenreSerializer
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = "__all__"

        read_only_fields = ["id"]

    def create(self, validated_data: dict) -> Movie:
        genre_data = validated_data.pop("genres")

        movie = Movie.objects.create(**validated_data)

        for genre in genre_data:
            get_genre, created = Genre.objects.get_or_create(**genre)
            movie.genres.add(get_genre)

        return movie

    def update(self, instance: Movie, validated_data: dict) -> Movie:

        for key, value in validated_data.items():
            if key == "genres":
                new_validated = validated_data.copy()
                genres_data = new_validated.pop("genres")
                instance.genres.set([])
                for genre in genres_data:
                    get_genre, created = Genre.objects.get_or_create(**genre)
                    instance.genres.add(get_genre)

            else:
                setattr(instance, key, value)

        instance.save()

        return instance
