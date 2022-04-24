from django.contrib import admin

# Register your models here.

from .models import Article
class adminArticle(admin.ModelAdmin):
    list_display = ['id','title','timestamp','updated']
    search_fields = [ 'title' ]


admin.site.register(Article,adminArticle)