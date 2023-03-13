from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    """Функция для выведения 10 записей на странице."""

    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'posts/index.html', context)


def group_post(request, slug):
    """Функция для отображения сообщения для страницы группы."""

    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:settings.NUM_REC]

    context = {
        'group': group,
        'posts': posts
    }
    return render(request, 'posts/group_list.html', context)
