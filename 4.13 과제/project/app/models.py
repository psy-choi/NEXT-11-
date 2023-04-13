from django.db import models

# Create your models here.
class Post(models.Model):
   title = models.CharField(max_length=50)
   content = models.TextField()


   def __str__(self):
       return self.title

class Comment(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') # comments를 하면 post.comments 로 가져올 수 있게 됨
   content = models.TextField()


   def __str__(self):
       return self.content

class InnerComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    def __str__(self):
       return self.content