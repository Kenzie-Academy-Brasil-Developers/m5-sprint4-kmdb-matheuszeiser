from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class RecomendationChoices(models.TextChoices):
    MUST_WATCH = "Must Watch"
    SHOULD_WATCH = "Should Watch"
    AVOID_WATCH = "Avoid Watch"
    DEFAULT = "No Opinion"


class Review(models.Model):
    stars = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    review = models.TextField()
    spoilers = models.BooleanField(null=True, default=False)
    recomendation = models.CharField(
        max_length=50,
        choices=RecomendationChoices.choices,
        default=RecomendationChoices.DEFAULT,
    )

    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="reviews", null=True
    )

    critic = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews", null=True
    )
