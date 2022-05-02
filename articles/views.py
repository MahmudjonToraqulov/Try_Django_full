from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
from django.http import Http404

# Create your views here.



def article_search_view(request):
    query = request.GET.get("q") 
    qs = Article.objects.search(query=query)
    context={
        'objects_list': qs
    }
    return render( request , 'articles/search.html',context=context )

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None) 
    context = {
        'form': form
    }
    if form.is_valid():
        article_obj = form.save()
        form = ArticleForm()
        print("vavava -> ", article_obj)
        return redirect(article_obj.get_absolute_url())
        context = { 
            'object': article_obj,
            'created': True
        }
    return render(request,'articles/create.html',context=context)


def article_detail_view( request , slug = None ):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug = slug)
        except Article.DoesNotExist:
            raise Http404
        except:
            raise Http404

    context = {
        "article_obj": article_obj
    }
    
    return render( request , 'articles/detail.html' , context=context )

