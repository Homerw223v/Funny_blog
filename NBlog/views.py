from django.shortcuts import render, redirect
from .forms import CommentForm, UserRegisterForm, BlogerUpdateForm, UserUpdateForm
from .models import Bloger, Post, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'NBlog/register.html', context={
        'form': form,
    })


@login_required
def about(request):
    return render(request, 'NBlog/about.html')


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'NBlog/home_page.html'
    context_object_name = 'posts'
    ordering = ['-post_date']
    paginate_by = 10
    queryset = Post.objects.select_related('author__bloger_name')


@login_required
def user_info(request, user_name):
    author = Bloger.objects.select_related('bloger_name').get(bloger_name=request.user)
    posts = Post.objects.select_related('author__bloger_name').filter(author__bloger_name=request.user)
    return render(request, 'NBlog/user_info.html', context={
        'author': author,
        'posts': posts,
    })


class BlogersListView(LoginRequiredMixin, ListView):
    model = Bloger
    template_name = 'NBlog/all_blogers.html'
    context_object_name = 'blogers'
    ordering = ['id']
    paginate_by = 10
    queryset = Bloger.objects.select_related('bloger_name')


@login_required
def all_blogs(request):
    posts = Post.objects.order_by('-post_date').select_related('author__bloger_name')
    return render(request, 'NBlog/all_blogs.html', context={
        'posts': posts,
    })


@login_required
def blog(request, blog_name):
    post = Post.objects.select_related('author__bloger_name').get(title=blog_name)
    comments = Comment.objects.select_related('post', 'author__bloger_name').filter(
        post=Post.objects.get(title=blog_name))
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user.bloger
            new_comment.save()
            return HttpResponseRedirect(reverse('blog-info', kwargs={'blog_name': blog_name}))
    comment_form = CommentForm()
    return render(request, 'NBlog/blog.html', context={
        'blog': post,
        'comment_form': comment_form,
        'comments': comments,
    })


@login_required
def update_profile(request):
    form = Bloger.objects.get(bloger_name=request.user)
    user_form = UserUpdateForm(instance=request.user)
    bloger_form = BlogerUpdateForm(instance=form)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        bloger_form = BlogerUpdateForm(request.POST,
                                       request.FILES,
                                       instance=request.user.bloger)
        if user_form.is_valid() and bloger_form.is_valid():
            user_form.save()
            bloger_form.save()
            messages.success(request, 'Information has been updated!')
            return redirect('user-info', request.user)
    return render(request, 'NBlog/profile_form.html', context={
        'user_form': user_form,
        'image_form': bloger_form,
    })


class CommentUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['comment']
    success_url = reverse_lazy('all-blogs')
    queryset = Comment.objects.select_related('post', 'author')

    def test_func(self):
        comment = self.get_object()
        if self.request.user.bloger == comment.author:
            return True
        return False


class CommentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('all-blogs')

    def test_func(self):
        comment = self.get_object()
        if self.request.user.bloger == comment.author:
            return True
        return False


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description']
    success_url = reverse_lazy('all-blogs')

    def form_valid(self, form):
        form.instance.author = self.request.user.bloger
        return super(PostCreate, self).form_valid(form)


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'description']
    success_url = reverse_lazy('all-blogs')

    def form_valid(self, form):
        form.instance.author = self.request.user.bloger
        return super(PostUpdate, self).form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user.bloger == post.author:
            return True
        return False


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('all-blogs')

    def test_func(self):
        post = self.get_object()
        if self.request.user.bloger == post.author:
            return True
        return False
