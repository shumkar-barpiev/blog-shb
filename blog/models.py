from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Categories(models.TextChoices):
    WEB_TECHNOLOGY = 'Веб-Технология'
    COMPUTER_GRAPHICS = 'Компьютердик Графика'
    PYTHON = 'Python '
    JAVASCRIPT = 'Javascript'
    JAVA = 'Java'
    DJANGO = 'Django'
    REACT_JS = 'React'
    LEARNING_METHODS = 'Үйрөнүү техникалары'
    SCIENCE = 'Илим'

# Create your models here.

class Post (models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.WEB_TECHNOLOGY)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey (User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager() #default manager
    newmanager = NewManager() #custom manager

    def get_absolute_url(self):
        return reverse('blog:post_single',args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title