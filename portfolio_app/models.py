from django.db import models

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

    def __str__(self):
        return self.name
