from collections import namedtuple
from pydoc import synopsis
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=127)
