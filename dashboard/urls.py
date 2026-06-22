from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('login/', views.DashboardLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='dashboard:login'), name='logout'),
    path('', views.overview, name='overview'),

    path('profile/', views.profile_edit, name='profile_edit'),

    path('skills/', views.skill_list, name='skill_list'),
    path('skills/add/', views.skill_form, name='skill_add'),
    path('skills/<int:pk>/edit/', views.skill_form, name='skill_edit'),
    path('skills/<int:pk>/delete/', views.skill_delete, name='skill_delete'),

    path('projects/', views.project_list, name='project_list'),
    path('projects/add/', views.project_form, name='project_add'),
    path('projects/<int:pk>/edit/', views.project_form, name='project_edit'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),

    path('experience/', views.experience_list, name='experience_list'),
    path('experience/add/', views.experience_form, name='experience_add'),
    path('experience/<int:pk>/edit/', views.experience_form, name='experience_edit'),
    path('experience/<int:pk>/delete/', views.experience_delete, name='experience_delete'),

    path('education/', views.education_list, name='education_list'),
    path('education/add/', views.education_form, name='education_add'),
    path('education/<int:pk>/edit/', views.education_form, name='education_edit'),
    path('education/<int:pk>/delete/', views.education_delete, name='education_delete'),

    path('certifications/', views.certification_list, name='certification_list'),
    path('certifications/add/', views.certification_form, name='certification_add'),
    path('certifications/<int:pk>/edit/', views.certification_form, name='certification_edit'),
    path('certifications/<int:pk>/delete/', views.certification_delete, name='certification_delete'),

    path('messages/', views.message_list, name='message_list'),
    path('messages/<int:pk>/', views.message_detail, name='message_detail'),
    path('messages/<int:pk>/delete/', views.message_delete, name='message_delete'),
]
