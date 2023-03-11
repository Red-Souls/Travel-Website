from django.shortcuts import render, redirect
from django.views import View
from .forms import*

# Create your views here.
class Home(View):
    def get(self, request):
        posts = Post.objects.all().order_by('-date')
        return render(request, 'blog.html', {
            'posts': posts
        })
    
class PostDetail(View):
    def get(self, request, id):
        post = Post.objects.get(id = id)
        comments = Comment.objects.filter(post = id).order_by('-date')
        return render(request, 'postDetail.html', {
            'post': post,
            'comments': comments,
        })
    
class AddComment(View):
    def get(self, request, id):
        form = AddCommentForm()
        return render(request, 'addComment.html', {'form': form})

    def post(self, request, id):
        form = AddCommentForm(request.POST)
        form.instance.post = Post.objects.get(id = id)
        form.instance.user = self.request.user
        if form.is_valid():
            form.save()
            return redirect('/blog/{}/'.format(id))
        return redirect('/blog/')