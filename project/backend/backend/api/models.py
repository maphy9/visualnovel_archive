from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
        ('user', 'User'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.username

class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class VisualNovel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    developer = models.CharField(max_length=255)
    # publisher = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    genres = models.ManyToManyField(Genre, related_name="visual_novels", blank=True)

    def __str__(self):
        return self.title
    
class Commit(models.Model):
    visual_novel = models.ForeignKey(VisualNovel, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.visual_novel.title}: {self.message}"