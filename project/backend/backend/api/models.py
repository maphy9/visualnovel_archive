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
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
    
class Developer(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class VisualNovel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    developer = models.ForeignKey(Developer, on_delete=models.SET_NULL, null=True, related_name="visual_novels")
    publishers = models.ManyToManyField(Publisher, related_name="visual_novels")
    genres = models.ManyToManyField(Genre, related_name="visual_novels")
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='visual_novel_images/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class Like(models.Model):
    visual_novel = models.ForeignKey(VisualNovel, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s like on {self.visual_novel.title}"
    
class Comment(models.Model):
    visual_novel = models.ForeignKey(VisualNovel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s comment on {self.visual_novel.title}"
    
class Discussion(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='discussions_images/')
    description = models.TextField()
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="discussions")

    def __str__(self):
        return f"Discussion: \"{self.title}\""
    
class Reply(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='discussions_images/', null=True, blank=True)
    reply_to = models.ForeignKey("Reply", on_delete=models.SET_NULL, null=True, blank=True)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name="replies")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="replies")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} reply to {self.discussion.title}"

class SideWindow(models.Model):
    image = models.ImageField(upload_to='articles_images/')
    text = models.TextField()

    def __str__(self):
        return self.text

class Paragraph(models.Model):
    order_number = models.IntegerField()
    title = models.CharField(max_length=255)
    text = models.TextField()
    side_window = models.ForeignKey(SideWindow, on_delete=models.SET_NULL, null=True, blank=True)
    visual_novel = models.ForeignKey(VisualNovel, on_delete=models.CASCADE, related_name="paragraphs")

    def __str__(self):
        return self.title
    
class Commit(models.Model):
    visual_novel = models.ForeignKey(VisualNovel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.visual_novel.title}: {self.message}"