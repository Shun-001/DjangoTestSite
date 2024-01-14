from django.shortcuts import render, redirect
from blogs.forms import CommentForm
from .models import Post

# Create your views here.

def toppage(request):
    posts = Post.objects.all()
    return render(request, 'blogs/toppage.html', {'posts':posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)  # postのデータベースの中のslug情報をpostに代入
    
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
        
    else:
        form = CommentForm()

    return render(request, 'blogs/post_detail.html', {'post':post, 'form':form})
