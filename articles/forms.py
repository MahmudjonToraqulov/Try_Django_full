from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [ 'title','content']
    
    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title',"\'title\' already exists")
        return data



class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        cleaned_data = self.cleaned_data 
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == 'office':
            self.add_error('title',f'That {title} is taken')
        if 'office' in content or 'office' in title.lower():
            self.add_error('content','title cannot be in content')
            raise forms.ValidationError('You can\'t write office ')
        return cleaned_data
