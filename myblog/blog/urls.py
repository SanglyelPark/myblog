
from django.urls import path

from blog import views

app_name = 'blog'
urlpatterns = [

    path('blog/', views.index, name='index'),
    # 상세페이지
    path('<int:post_id>/', views.detail, name='detail'),
    # 카테고리
    path('category/<str:slug>/', views.category_page, name='category_page'),
    # 포스트 쓰기
    path('post/create/', views.post_create, name='post_create'),
]
