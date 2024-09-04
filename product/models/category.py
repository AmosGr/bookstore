from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,)
    description = models.CharField(max_length=200,blank=True,null=True)
    active = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            num = 1
            while Category.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)


    def __unicode__(self):
        return self.title