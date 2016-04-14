from django.shortcuts import render, HttpResponse
from .models import Post
from django.utils import timezone

# Create your views here.

def test(request):
    return HttpResponse('Test OK!')

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now() ).order_by('-published_date')
    return render(request, "blogposts.html",{'posts' : posts } )