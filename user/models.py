from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='почта', unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name='телефон')
    country = models.CharField(max_length=100, blank=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
