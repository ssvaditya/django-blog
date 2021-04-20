from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from blog.models import Post, Comment

def home(request):
    context = {
            'posts' : Post.objects.all()
            }
    
    return render(request,'blog/home.html',context)

# CREATING CLASS BASED VIEW:
#     1)import type of view(ListView)
#     2)create class and specify what model you want to display
#   * 3)specify template_name (because django looks for specific kind of name of template by default:<app>/<model>_<viewtype>.html
 
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']    
    paginate_by = 5
    
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddCommentView(CreateView):
        model = Comment
        fields = ['name','body']
        template_name = 'blog/add_comment.html'
        
        def form_valid(self, form):

            form.instance.post_id = self.kwargs['pk']
            return super().form_valid(form)

def like_post(request, pk):
    post=get_object_or_404(Post, pk=pk)
    post.likes+=1
    post.save()
    return redirect('post-detail', pk=post.pk)
        
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
   
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Post
        success_url = '/' 

        def test_func(self):
            post = self.get_object()
            if self.request.user == post.author:
                return True
            return False

def about(request):
    return render(request,'blog/about.html',{'title':'About'})





