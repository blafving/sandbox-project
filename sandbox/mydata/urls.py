from django.urls import path

from . import views

app_name = 'mydata'
urlpatterns = [
    path('', views.home, name='index'),
    path('importmyfitpal/', views.import_myfitpal, name='import'),
    path('importmyfitpal/working/', views.working, name='valid'),
    path('importmyfitpal/notworking/', views.notworking, name='import'),
    path('<int:username>/', views.user, name='user'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
