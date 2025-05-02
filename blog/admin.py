from django.contrib import admin
from .models import Article, Contact

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_creation', 'date_publication')
    list_filter = ('date_creation', 'date_publication', 'auteur')
    search_fields = ('titre', 'contenu')
    ordering = ('-date_creation',)
    date_hierarchy = 'date_creation'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'date_envoi')
    list_filter = ('date_envoi',)
    search_fields = ('nom', 'email', 'sujet', 'message')
    ordering = ('-date_envoi',)