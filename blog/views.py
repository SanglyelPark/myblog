from django.shortcuts import render, get_object_or_404

from blog.models import Post


def index(request):
    # 포스트 목록
    post_list = Post.objects.all()
    context = {'post_list': post_list }
    return render(request, 'blog/post_list.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)
