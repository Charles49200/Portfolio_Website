<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Project, WorkExperience, ContactSubmission, Blog, Topic
from django.contrib.auth.forms import UserCreationForm
from .forms import BlogForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import os

def dashboard(request):
    # Fetch data to pass to the template
    projects = Project.objects.all()
    experiences = WorkExperience.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True)[:5]
    recent_posts = Blog.objects.all().order_by('-created_at')[:5]
    topics = Topic.objects.all()

    # user_profile = None
    # if request.user.is_authenticated:
    #     user_profile = UserProfile.objects.filter(user=request.user).first()

    return render(request, 'index.html', {
        'projects': projects,
        'experiences': experiences,
        'featured_posts': featured_posts,
        'recent_posts': recent_posts,
        'topics': topics,
        # 'user_profile': user_profile,
    })

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog.html', {'form': form})

@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, author=request.user)
    blog.delete()
    return redirect('blog_list')

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    blogs = Blog.objects.filter(topic=topic)
    return render(request, 'blog.html', {'topic': topic, 'blogs': blogs})

def post_detail(request, post_id):
    post = get_object_or_404(Blog, id=post_id)
    return render(request, 'blog.html', {'post': post})


def contact_view(request):
    context = {}
=======
from django.shortcuts import render, redirect
from .models import Project, WorkExperience, ContactSubmission
from django.http import HttpResponse, Http404
from django.conf import settings
import os

def dashboard(request):
    projects = Project.objects.all()
    for p in projects:
        print(f"Found {p} with image {p.image.url}")
    experiences = WorkExperience.objects.all()
    return render(request, 'index.html', {
        'projects': projects,
        'experiences': experiences,
    })

def contact_view(request):
>>>>>>> 388fceab (First commit)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')  # If you're using it
        message = request.POST.get('message')

        # Save the data to the database
        ContactSubmission.objects.create(
            name=name,
            email=email,
<<<<<<< HEAD
            subject=subject,
            message=message
        )
        return redirect('success')  # Redirect after successful submission

    return render(request, 'index.html', context)  # Your contact template
=======
            subject =subject,
            message=message
        )
        context = {'success_message': 'Your message has been successfully submitted!'}

        return redirect('success')  # Redirect after successful submission

    return render(request, 'index.html', context) # Your contact template
>>>>>>> 388fceab (First commit)

def submissions_view(request):
    submissions = ContactSubmission.objects.all().order_by('-submitted_at')
    return render(request, 'submissions.html', {'submissions': submissions})

<<<<<<< HEAD
=======

>>>>>>> 388fceab (First commit)
def success_view(request):
    return render(request, 'index.html')  # Create a success.html template

def download_cv(request):
    file_path = os.path.join(settings.STATIC_ROOT, 'Charles_Irungu_CV_letter.docx')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
<<<<<<< HEAD
            response = HttpResponse(
                file.read(),
                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            )
            response['Content-Disposition'] = 'attachment; filename="Charles_Irungu_CV_letter.docx"'
            return response
    else:
        raise Http404("File not found")

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})

@login_required 
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'index.html', {'form': form})

@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, author=request.user)
    blog.delete()
    return redirect('blog_list')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'index.html', {'form': form})

def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        
        if User.objects.filter(username=username).exists():
            messages.error("Username already taken. Use another one")
            return render(request, "signup.html")
        if password2 != password1:
            messages.error("Passwords do not match")
            return render(request, "signup.html")
        
        user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname)
        user.set_password(password1)
        user.save()
   
        messages.success(request, f'Account created successfully! You can now log in.')
        return render(request, "index.html")


def signup2(request):
    
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('dashboard')  # Redirect to the dashboard or desired page
        else:
            # Invalid credentials
            messages.error(request, 'Invalid username or password. Please try again.')
            return render(request, 'signup.html')

    # GET request, render the login form
    return render(request, 'signup.html')

def signup3(request):
    # Your logic for the signup3 view
    return render(request, 'signup.html')

def blog_view(request):
    blogs = Blog.objects.all()  # Example of fetching blog data from the database
    return render(request, 'blog.html', {'blogs': blogs})
=======
            response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename="Charles_Irungu_CV_letter.docx"'
            return response
    else:
        raise Http404("File not found")
>>>>>>> 388fceab (First commit)
