from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, BlogForm
from .models import Blog



def home(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(user=request.user)
        return render(request, 'home.html', {'blogs': blogs})
    else:
        return render(request, 'home.html')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('blog_detail', pk=blog.pk)  # Redirect to the blog detail page
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.views += 1
    blog.save()
    return render(request, 'blog_detail.html', {'blog': blog})

@login_required
def update_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=pk)  # Redirect to the blog detail page
    else:
        form = BlogForm(instance=blog)
    return render(request, 'update_blog.html', {'form': form})

@login_required
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('home')  # Redirect to the home page after deletion
    return render(request, 'delete_blog.html', {'blog': blog})
