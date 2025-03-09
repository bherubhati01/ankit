from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profileImage',blank=True,null=True,default='profile.png')
    bio = models.TextField(blank=True,null=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='following')
    friends = models.ManyToManyField('Friend', related_name='my_friends')

class Post(models.Model):
    user = models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)
    post = models.ImageField(upload_to='posts',blank=True,null=True)
    caption = models.TextField(blank=True,null=True)    
    likes = models.ManyToManyField(User, related_name='liked_posts')
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def number_of_likes(self):
        return self.likes.count()

    def number_of_posts(self):
        return self.post.count()

    def __str__(self):
        return f"Post {self.id} by {self.user.username}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments',default='post.png')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    text = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.text}"
    

class Friend(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.first_name   
    

class ChatMessage(models.Model):
    body = models.TextField()
    msg_sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='msg_sender')
    msg_receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='msg_receiver')
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.body
    

