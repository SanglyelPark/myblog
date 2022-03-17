
from django.urls import path

from blog import views

app_name = 'blog'
urlpatterns = [

    path('blog/', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail')
]
