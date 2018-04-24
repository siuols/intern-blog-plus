from django.db import models

from django.db.models.signals import pre_save

from django.conf import settings

from .utils import unique_slug_generator

User = settings.AUTH_USER_MODEL

# Create your models here.

class Tag(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    title                   = models.CharField(max_length=120)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)
    slug                    = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.title)

    @property
    def slug_title(self):
        return '{}'.format(self.title)

class Category(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    title                   = models.CharField(max_length=120)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)
    slug                    = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.title)

    @property
    def slug_title(self):
        return '{}'.format(self.title)

STATUS_CHOICES = (
    ('published', 'Published'),
    ('draft', 'Draft'),
    ('hidden', 'Hidden')
)

class Post(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    title                   = models.CharField(max_length=255)
    subtitle                = models.CharField(max_length=255)
    banner_photo            = models.ImageField()
    tags                    = models.ManyToManyField(Tag)
    category                = models.ForeignKey('Category', on_delete=models.CASCADE)
    body                    = models.TextField()
    status                  = models.CharField(
                                                max_length=9,
                                                choices=STATUS_CHOICES,
                                                default='published'
                                            )
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)
    slug                    = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['-id']

    @property
    def slug_title(self):
        return '{}'.format(self.title)

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Post)
pre_save.connect(rl_pre_save_receiver, sender=Category)
pre_save.connect(rl_pre_save_receiver, sender=Tag)
