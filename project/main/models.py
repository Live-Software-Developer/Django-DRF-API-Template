from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Contact(models.Model):

    name = models.CharField(max_length=50, blank=False, null=True)
    email = models.EmailField(max_length=50, blank=False, null=True)
    phone_no = models.CharField(max_length=50, blank=False, null=True)
    service = models.CharField(max_length=50, blank=False, null=True)
    other = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=150, blank=False, null=True)
    message = models.TextField(blank=False, null=True)

    created_on = models.DateTimeField(auto_now_add=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject} {self.name}"


class BlogCategory(models.Model):
    title = models.CharField(max_length=50, blank=False, null=True)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Blog Categories'

    def __str__(self):
        return f'category_{self.id}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(BlogCategory, self).save(*args, **kwargs)


class BlogTag(models.Model):
    title = models.CharField(max_length=50, blank=False, null=True)
    slug = models.SlugField(blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Blog Tags'

    def __str__(self):
        return f'tag_{self.id}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(BlogTag, self).save(*args, **kwargs)


class Blog(models.Model):
    user = models.ForeignKey(User, blank=False, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255, blank=False, null=True)
    slug = models.CharField(max_length=300, blank=True, null=False, default="")
    keywords = models.TextField(blank=False, null=True)
    description = models.TextField(blank=False, null=True)
    categories = models.ManyToManyField(BlogCategory, blank=True)
    tags = models.ManyToManyField(BlogTag, blank=True)
    details = models.JSONField(blank=False, null=True)
    image = models.URLField(blank=False, null=True)
    image_alt_text = models.CharField(max_length=200, blank=False, null=True)

    created_on = models.DateTimeField(auto_now_add=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Blog, self).save(*args, **kwargs)


class BlogReply(models.Model):
    user = models.ForeignKey(User, blank=False, null=True, on_delete=models.SET_NULL)
    blog = models.ForeignKey(Blog, related_name='replies', blank=False, null=True, on_delete=models.SET_NULL)
    details = models.JSONField(blank=False, null=True)

    created_on = models.DateTimeField(auto_now_add=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Review(models.Model):
    user = models.ForeignKey(User, blank=False, null=True, on_delete=models.SET_NULL)
    review = models.TextField(blank=False, null=True)
    rating = models.FloatField(blank=False)

    created_on = models.DateTimeField(auto_now_add=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Media(models.Model):
    title = models.CharField(blank=True, null=True, max_length=60)
    file = models.FileField(blank=False, null=True)
    type = models.CharField(max_length=20, blank=False, null=True)

    created_on = models.DateTimeField(auto_now_add=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'media_{self.id}'

