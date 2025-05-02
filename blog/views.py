from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Article
from .forms import ContactForm

def accueil(request):
    articles = Article.objects.filter(
        date_publication__lte=timezone.now()
    ).order_by('-date_publication')[:5]
    return render(request, 'blog/accueil.html', {'articles': articles})

def liste_articles(request):
    articles = Article.objects.filter(
        date_publication__lte=timezone.now()
    ).order_by('-date_publication')
    return render(request, 'blog/liste_articles.html', {'articles': articles})

def detail_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/detail_article.html', {'article': article})

from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    
    return render(request, 'blog/contact.html', {'form': form})
