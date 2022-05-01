from django.db import models
# Create your models here.
from django.db.models.signals import pre_save , post_save
from .utils import slugify_instance_title

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    slug = models.CharField(unique=True,max_length=50,blank=True,null=True)
    timestamp = models.DateTimeField( auto_now_add=True )
    updated = models.DateTimeField( auto_now=True )
    publish = models.DateField( auto_now_add=False, auto_now=False, blank=True, null=True )

    def save(self,*args,**kwargs):
        if self.slug is None:
            slugify_instance_title(self,save=False)
        super().save(*args,**kwargs)




def article_pre_save(sender , instance , *args , **kwargs):
    print(sender)
    if instance.slug is None:
        slugify_instance_title(instance,save=False)

pre_save.connect(article_pre_save,sender=Article)


def article_post_save(sender , instance , created , *args , **kwargs):
    if created:
        slugify_instance_title(instance,save=True) 

post_save.connect(article_post_save,sender=Article)