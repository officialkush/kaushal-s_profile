from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('skills/', views.skills, name='skills'),

    path('projects/', views.projects, name='projects'),

    # Dynamic project detail page
    path(
        'projects/<int:pk>/',
        views.project_detail,
        name='project_detail'
    ),

    path('experience/', views.experience, name='experience'),

    path('contact/', views.contact, name='contact'),

    path(
        'robots.txt',
        views.robots_txt,
        name='robots'
    ),
]