from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name='accueil'),
    path('blog/', views.liste_articles, name='liste_articles'),
    path('article/<int:pk>/', views.detail_article, name='detail_article'),
    path('contact/', views.contact, name='contact'),

]

