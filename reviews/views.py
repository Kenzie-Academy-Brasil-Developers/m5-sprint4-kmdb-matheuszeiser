from django.shortcuts import get_object_or_404, render
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Request, Response, status

from movies.models import Movie
from reviews.models import Review
from reviews.permissions import IsAdmOrCriticOrSafeMethod, IsCriticOwner
from reviews.serializers import ReviewSerializer


class MoreThan1ReviewError(Exception):
    ...


class ReviewView(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmOrCriticOrSafeMethod]

    def get(self, request: Request, movie_id: int) -> Response:
        reviews = Review.objects.filter(movie=movie_id)
        result_page = self.paginate_queryset(reviews, request, view=self)

        serializer = ReviewSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        reviews = Review.objects.filter(movie_id=movie.id, critic=request.user.id)

        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            if len(reviews) > 0:
                raise MoreThan1ReviewError
        except MoreThan1ReviewError:
            return Response({"detail": "Just one review per movie"})

        serializer.save(critic=request.user, movie=movie)

        return Response(serializer.data)


class ReviewDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmOrCriticOrSafeMethod, IsCriticOwner]

    def get(self, request: Request, movie_id: int, review_id: int) -> Response:
        review = get_object_or_404(Review, id=review_id)

        serializer = ReviewSerializer(review)

        return Response(serializer.data)

    def delete(self, request: Request, movie_id: int, review_id: int) -> Response:
        review = get_object_or_404(Review, id=review_id)

        self.check_object_permissions(request, review)

        # review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
