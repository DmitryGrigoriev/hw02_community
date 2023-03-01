from django.conf import settings
from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    """Функция для выведения 10 последних записей."""

    posts = Post.objects.all()[:settings.NUM_REC]

    context = {
        'posts': posts
    }

    return render(request, 'posts/index.html', context)


def group_post(request, slug):
    """Функция для отображения сообщения для страницы группы."""

    group = get_object_or_404(Group, slug=slug)
    posts = group.groups.all()[:settings.NUM_REC]

    context = {
        'group': group,
        'posts': posts
    }
    return render(request, 'posts/group_list.html', context)
