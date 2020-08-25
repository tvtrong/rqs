from django.db import models


class Post(models.Model):
    title = models.CharField(default='Article title', max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg', upload_to='post_imgs/')
    text = models.TextField(default='text')

    def __str__(self):
        return self.title

    def short_text(self):
        return self.text[:60]+'...'

    class Meta:
        ordering = ['-date']
