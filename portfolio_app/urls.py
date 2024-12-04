from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('contact/', views.contact_view, name='contact'),
    path('submissions/', views.submissions_view, name='submissions'),
    path('success/', views.success_view, name='success'),
]
