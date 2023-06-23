from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.


class Bloger(models.Model):
    GENRE = (
        ('M', 'Male'),
        ('F', "Female"),
        ('U', 'Undefined')
    )
    bloger_name = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    date_of_birth = models.DateField(default=None, null=True, )
    bloger_bio = models.TextField(max_length=500, blank=True, verbose_name='Biography',
                                  help_text='Write about yourself')
    genre = models.CharField(max_length=1, choices=GENRE, default='U', help_text='Your Genre')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.bloger_name}"

    def get_absolute_url(self):
        return reverse('user-info', args=[str(self.bloger_name)])

    def save(self, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Post(models.Model):
    title = models.CharField(max_length=200, help_text='Come up with a title', )
    post_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=200000, help_text='Write your post here', verbose_name='Content')
    author = models.ForeignKey(Bloger, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Bloger, on_delete=models.PROTECT, null=True)
    post_date = models.DateTimeField(max_length=50, default=datetime.now())
    comment = models.TextField(max_length=1000, help_text='Write your comment')

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

    def get_absolute_url(self):
        return reverse('comment', args=[str(self.id)])
