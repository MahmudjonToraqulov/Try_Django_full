from django.db import models
# Create your models here.
from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    slug = models.CharField(max_length=50,blank=True,null=True)
    timestamp = models.DateTimeField( auto_now_add=True )
    updated = models.DateTimeField( auto_now=True )
    publish = models.DateField( auto_now_add=False, auto_now=False, blank=True, null=True )

    def save(self,*args,**kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)

