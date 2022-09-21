from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm, PictureForm
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from cloudinary.forms import cl_init_js_callbacks

# Create your views here.


def index(request):
    # if the methode is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        print("hello world")
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')
        else:

            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]

    # show
    return render(request, 'posts.html',
                  {'posts': posts})


def delete(request, post_id):
    # First post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    form = PostForm
    return render(request, 'edit.html', {'post': post, 'form': form})


def LikeView(request, post_id):
    post = Post.objects.get(id=post_id)
    new_value = post.likes + 1
    post.likes = new_value
    post.save()
    return HttpResponseRedirect('/')
