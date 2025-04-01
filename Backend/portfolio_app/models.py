from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User
=======
>>>>>>> 388fceab (First commit)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    view_link = models.URLField(max_length=300)
    source_link = models.URLField(max_length=300)

    def __str__(self):
        return self.title

class WorkExperience(models.Model):
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='experiences/', blank=True, null=True)
    company = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.role

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255, default="No Subject")  # Add default here
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

<<<<<<< HEAD
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.user.username

class Topic(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='topics/')

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(default='', blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/', default='default_blog_image.jpg')  # Add a default image here
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
=======
    def __str__(self):
        return self.name
>>>>>>> 388fceab (First commit)
