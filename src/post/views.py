from django.shortcuts import render , get_object_or_404 , redirect
from . models import Post
from . forms import PostForm

# Create your views here.


def all_posts(request) :
    all_posts= Post.objects.filter(active=True)

    context = {
        'all_posts' : all_posts,
    }

    return render(request, 'all_posts.html', context)


def post(request, id) :
    # post= Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)

    context= {
        'post' : post,
    }

    return render(request, 'post.html', context)



def create_post(request) :
    if request.method == 'POST' :
        form = PostForm(request.POST)
        if form.is_valid() :
            new_form= form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/')


    else :
        form = PostForm()

    context = {
        'form' : form
    }

    
    return render(request, 'CreatePost.html', context)



def edit_post(request, id) :
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST' :
        form = PostForm(request.POST, instance= post)
        if form.is_valid() :
            new_form= form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/')


    else :
        form = PostForm(instance= post)

    context = {
        'form' : form
    }

    
    return render(request, 'EditPost.html', context)