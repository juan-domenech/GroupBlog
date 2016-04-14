from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.utils import timezone
from .models import Post

def test(request):
    return HttpResponse('Test OK!')

def no_path(request):
    return redirect('/blog/')

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now() ).order_by('-published_date')
    return render(request, "blogposts.html",{'posts' : posts } )

def post_detail(request,id):
    post = get_object_or_404(Post,pk=id)
    # clock up the number of post views
    post.views += 1
    post.save()
    return render(request, "blogdetail.html",{'post' : post} )
