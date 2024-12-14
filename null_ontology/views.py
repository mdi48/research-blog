from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404
from .models import Post

def main(request):
    template = loader.get_template(template_name='__main.html')
    return HttpResponse(content=template.render())

def browse(request, category):
    valid_categories = ['fiction', 'theory']
    if category not in valid_categories:
        raise Http404("Invalid category")
    page = int(request.GET.get('page', 1))
    items_per_page = 9
    start = (page - 1) * items_per_page
    end = start + items_per_page
    all_posts = Post.objects.filter(category=category)
    posts = all_posts[start:end]
    total_pages = (all_posts.count() + items_per_page - 1) // items_per_page
    page_nums = list(range(1, total_pages + 1))
    return render(request=request, template_name='__browse.html', context={
        'posts': posts,
        'category': category,
        'current_page': page,
        'total_pages': total_pages,
        'page_nums': page_nums
    })



def content(request, category, post_slug):
    post = get_object_or_404(klass=Post, category=category, slug=post_slug)
    return render(request=request, template_name='__content.html', context={'post': post})

