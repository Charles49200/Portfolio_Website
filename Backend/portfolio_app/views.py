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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')  # If you're using it
        message = request.POST.get('message')

        # Save the data to the database
        ContactSubmission.objects.create(
            name=name,
            email=email,
            subject =subject,
            message=message
        )
        context = {'success_message': 'Your message has been successfully submitted!'}

        return redirect('success')  # Redirect after successful submission

    return render(request, 'index.html', context) # Your contact template

def submissions_view(request):
    submissions = ContactSubmission.objects.all().order_by('-submitted_at')
    return render(request, 'submissions.html', {'submissions': submissions})


def success_view(request):
    return render(request, 'index.html')  # Create a success.html template

def download_cv(request):
    file_path = os.path.join(settings.STATIC_ROOT, 'Charles_Irungu_CV_letter.docx')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename="Charles_Irungu_CV_letter.docx"'
            return response
    else:
        raise Http404("File not found")