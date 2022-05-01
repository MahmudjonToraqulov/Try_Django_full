# from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from articles.models import Article
from django.template.loader import render_to_string


def home_view(request):
    """ Home view """
    name = 'justin'
    number = randint(1,2)
    # Database
    
    article = Article.objects.all()

    context = {
        'article': article
    }

    HTML_STRING =  render_to_string( 'salom.html' , context=context )

    return HttpResponse( HTML_STRING )
