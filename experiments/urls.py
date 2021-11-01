from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:experiment_id>/', views.detail, name='detail'),
    path('<int:experiment_id>/results/', views.results, name='results'),
    path('<int:experiment_id>/vote/', views.vote, name='vote'),
]
