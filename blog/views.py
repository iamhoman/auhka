from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.text import slugify
from django.conf import settings
import time
from .models import Post, Post_isLike
from .forms import post_create_form, post_like_form, post_comment_form
import os
from PIL import Image

def post_list(request):

    posts = Post.objects.filter(status='published')

    post_paginator = Paginator(posts, 3)
    page_num = request.GET.get('page')

    page = post_paginator.get_page(page_num)

    context = {
        'post_count': post_paginator.count,
        'page_tot': post_paginator.num_pages,
        'page': page
    }

    return render(request, 'blog/post_list.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'blog/post/../templates/blog/post_detail.html',
                  {'post': post})

def upload_handler(f, loc):
    with open(loc, 'wb+') as destination:
        for chunk in f.chunks:
            destination.write(chunk)


@login_required(login_url="/accounts/login/")
def post_create(request):
    if request.method == "POST":
        form = post_create_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.status = 'published'
            post.save()
            post = Post.objects.first()
            post_pk_05d = format(post.pk, '05d')

            if len(request.FILES) > 0:
                for k in request.FILES.keys():
                    print (k)
                    pic = request.FILES.get(k)
                    pic_fmt = pic.name.split('.')[-1]
                    pic_path = '/blog/post_' + post_pk_05d + '_' + time.strftime('%Y%m%d') + '_' + k + '.' + pic_fmt
                    with open(settings.MEDIA_ROOT + pic_path, 'wb+') as destination:
                        for chunk in pic.chunks():
                            destination.write(chunk)
                    image = Image.open(settings.MEDIA_ROOT + pic_path)
                    image.save (settings.MEDIA_ROOT + pic_path, quality=50)

                    if k == 'pic01': post.pic01 = pic_path
                    if k == 'pic02': post.pic02 = pic_path
                    if k == 'pic03': post.pic03 = pic_path
                    if k == 'pic04': post.pic04 = pic_path
                    post.save()

            return redirect('blog:post_list')
    else:
        form = post_create_form()
    return render(request, 'blog/post_create.html', {'form':form})

@user_passes_test(lambda u: u.is_superuser, login_url='/accounts/login/')
def post_delete(request, id):
    context = {}
    obj = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        # del pic01
        if bool(obj.pic01)==True:
            pic01_path = settings.MEDIA_ROOT + obj.pic01.name
            if os.path.exists(pic01_path): os.remove (pic01_path)

        # del pic02
        if bool(obj.pic02) == True:
            pic02_path = settings.MEDIA_ROOT + obj.pic02.name
            if os.path.exists(pic02_path): os.remove(pic02_path)

        # del pic03
        if bool(obj.pic03) == True:
            pic03_path = settings.MEDIA_ROOT + obj.pic03.name
            if os.path.exists(pic03_path): os.remove(pic03_path)

        # del pic04
        if bool(obj.pic04) == True:
            pic04_path = settings.MEDIA_ROOT + obj.pic04.name
            if os.path.exists(pic04_path): os.remove(pic04_path)

        # del obj
        obj.delete()

        # redirect to post_list
        return redirect('blog:post_list')
    else:
        return render(request, 'blog/post_delete.html', context)


@login_required(login_url="/accounts/login/")
def post_like(request, post_id):
    if request.method == "POST":
        form = post_like_form(request.POST)
        if form.is_valid():
            post_like = form.save(commit=False)
            post_like.liker = request.user
            post_like.post = Post.objects.get(id=post_id)
            if Post_isLike.objects.all().filter(liker=request.user).filter(post=post_id).count() == 0:
                post_like.save()
            return redirect('blog:post_list')
    else:
        form = post_like_form()
    return render(request, 'blog/post_like.html', {'form':form})

@login_required(login_url="/accounts/login/")
def post_comment(request, post_id):
    if request.method == "POST":
        form = post_comment_form(request.POST)
        if form.is_valid():
            post_comment = form.save(commit=False)
            post_comment.commenter = request.user
            post_comment.post = Post.objects.get(id=post_id)
            post_comment.save()
            return redirect('blog:post_list')
    else:
        form = post_comment_form()
    return render(request, 'blog/post_comment.html', {'form':form})
