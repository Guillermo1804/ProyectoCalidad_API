from django.db import models # type: ignore
from django.db.models.signals import post_save # type: ignore
from django.dispatch import receiver # type: ignore
from rest_framework.authentication import TokenAuthentication # type: ignore
from django.contrib.auth.models import AbstractUser, User # type: ignore
from django.conf import settings # type: ignore

