from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('portrait-photography', views.portrait_photography, name='portrait-photography'),
    path('report-photography', views.report_photography, name='report-photography'),
    path('genre-photography', views.genre_photography, name='genre-photography'),
    path('street-photography', views.street_photography, name='street-photography'),
    path('bw-photography', views.bw_photography, name='bw-photography'),
]