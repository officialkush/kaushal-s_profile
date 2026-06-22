from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages as dj_messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm

from core.models import Profile, Skill, Project, Experience, Education, Certification, Message
from .forms import (ProfileForm, SkillForm, ProjectForm, ExperienceForm,
                     EducationForm, CertificationForm)


# ---------------- AUTH ----------------

class DashboardLoginView(auth_views.LoginView):
    template_name = 'dashboard/login.html'
    redirect_authenticated_user = True

    def form_invalid(self, form):
        dj_messages.error(self.request, "Invalid username or password.")
        return super().form_invalid(form)


# ---------------- OVERVIEW ----------------

@login_required
def overview(request):
    context = {
        'profile': Profile.objects.first(),
        'skills_count': Skill.objects.count(),
        'projects_count': Project.objects.count(),
        'experience_count': Experience.objects.count(),
        'education_count': Education.objects.count(),
        'cert_count': Certification.objects.count(),
        'unread_messages': Message.objects.filter(read=False).count(),
        'total_messages': Message.objects.count(),
        'recent_messages': Message.objects.all()[:5],
    }
    context['active'] = 'overview'
    context['quick_links'] = [
        ('Edit Profile', 'fas fa-id-badge', '/dashboard/profile/'),
        ('Add Project', 'fas fa-plus', '/dashboard/projects/add/'),
        ('Add Skill', 'fas fa-sliders', '/dashboard/skills/add/'),
        ('Add Experience', 'fas fa-briefcase', '/dashboard/experience/add/'),
        ('Add Education', 'fas fa-graduation-cap', '/dashboard/education/add/'),
        ('Add Certification', 'fas fa-certificate', '/dashboard/certifications/add/'),
    ]
    return render(request, 'dashboard/overview.html', context)


# ---------------- PROFILE ----------------

@login_required
def profile_edit(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            dj_messages.success(request, 'Profile updated successfully.')
            return redirect('dashboard:profile_edit')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'dashboard/profile_form.html', {'form': form, 'active': 'profile'})


# ---------------- SKILLS ----------------

@login_required
def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'dashboard/skill_list.html', {'skills': skills, 'active': 'skills'})


@login_required
def skill_form(request, pk=None):
    instance = get_object_or_404(Skill, pk=pk) if pk else None
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            dj_messages.success(request, 'Skill saved.')
            return redirect('dashboard:skill_list')
    else:
        form = SkillForm(instance=instance)
    return render(request, 'dashboard/skill_form.html', {'form': form, 'instance': instance, 'active': 'skills'})


@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        dj_messages.success(request, 'Skill deleted.')
        return redirect('dashboard:skill_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': skill, 'cancel_url': 'dashboard:skill_list', 'active': 'skills'})


# ---------------- PROJECTS ----------------

@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'dashboard/project_list.html', {'projects': projects, 'active': 'projects'})


@login_required
def project_form(request, pk=None):
    instance = get_object_or_404(Project, pk=pk) if pk else None
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            dj_messages.success(request, 'Project saved.')
            return redirect('dashboard:project_list')
    else:
        form = ProjectForm(instance=instance)
    return render(request, 'dashboard/project_form.html', {'form': form, 'instance': instance, 'active': 'projects'})


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        dj_messages.success(request, 'Project deleted.')
        return redirect('dashboard:project_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': project, 'cancel_url': 'dashboard:project_list', 'active': 'projects'})


# ---------------- EXPERIENCE ----------------

@login_required
def experience_list(request):
    experiences = Experience.objects.all()
    return render(request, 'dashboard/experience_list.html', {'experiences': experiences, 'active': 'experience'})


@login_required
def experience_form(request, pk=None):
    instance = get_object_or_404(Experience, pk=pk) if pk else None
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            dj_messages.success(request, 'Experience saved.')
            return redirect('dashboard:experience_list')
    else:
        form = ExperienceForm(instance=instance)
    return render(request, 'dashboard/experience_form.html', {'form': form, 'instance': instance, 'active': 'experience'})


@login_required
def experience_delete(request, pk):
    exp = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        exp.delete()
        dj_messages.success(request, 'Experience deleted.')
        return redirect('dashboard:experience_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': exp, 'cancel_url': 'dashboard:experience_list', 'active': 'experience'})


# ---------------- EDUCATION ----------------

@login_required
def education_list(request):
    education = Education.objects.all()
    return render(request, 'dashboard/education_list.html', {'education': education, 'active': 'education'})


@login_required
def education_form(request, pk=None):
    instance = get_object_or_404(Education, pk=pk) if pk else None
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            dj_messages.success(request, 'Education saved.')
            return redirect('dashboard:education_list')
    else:
        form = EducationForm(instance=instance)
    return render(request, 'dashboard/education_form.html', {'form': form, 'instance': instance, 'active': 'education'})


@login_required
def education_delete(request, pk):
    edu = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        edu.delete()
        dj_messages.success(request, 'Education deleted.')
        return redirect('dashboard:education_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': edu, 'cancel_url': 'dashboard:education_list', 'active': 'education'})


# ---------------- CERTIFICATIONS ----------------

@login_required
def certification_list(request):
    certifications = Certification.objects.all()
    return render(request, 'dashboard/certification_list.html', {'certifications': certifications, 'active': 'certifications'})


@login_required
def certification_form(request, pk=None):
    instance = get_object_or_404(Certification, pk=pk) if pk else None
    if request.method == 'POST':
        form = CertificationForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            dj_messages.success(request, 'Certification saved.')
            return redirect('dashboard:certification_list')
    else:
        form = CertificationForm(instance=instance)
    return render(request, 'dashboard/certification_form.html', {'form': form, 'instance': instance, 'active': 'certifications'})


@login_required
def certification_delete(request, pk):
    cert = get_object_or_404(Certification, pk=pk)
    if request.method == 'POST':
        cert.delete()
        dj_messages.success(request, 'Certification deleted.')
        return redirect('dashboard:certification_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': cert, 'cancel_url': 'dashboard:certification_list', 'active': 'certifications'})


# ---------------- MESSAGES ----------------

@login_required
def message_list(request):
    msgs = Message.objects.all()
    return render(request, 'dashboard/message_list.html', {'messages_list': msgs, 'active': 'messages'})


@login_required
def message_detail(request, pk):
    msg = get_object_or_404(Message, pk=pk)
    if not msg.read:
        msg.read = True
        msg.save()
    return render(request, 'dashboard/message_detail.html', {'msg': msg, 'active': 'messages'})


@login_required
def message_delete(request, pk):
    msg = get_object_or_404(Message, pk=pk)
    if request.method == 'POST':
        msg.delete()
        dj_messages.success(request, 'Message deleted.')
        return redirect('dashboard:message_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': msg, 'cancel_url': 'dashboard:message_list', 'active': 'messages'})
