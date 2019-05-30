from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Blog
from .forms import PhotoForm

def index(request):
    blog_list = Blog.objects.order_by('-created_datetime')
    page = request.GET.get('page',1)

    paginator = Paginator(blog_list,1)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return render(request, 'blogs/index.html', {'blogs': blogs})

    if request.method == 'GET':
        return render(request, 'blogs/index.html', {
                'form': PhotoForm(),
            })

def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog':blog})
