from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Profile, Skill, Project, Experience, Education, Certification, Message


def get_profile():
    return Profile.objects.first()


def grouped_skills():
    skills = Skill.objects.all()
    grouped = {}
    for skill in skills:
        cat = skill.get_category_display()
        grouped.setdefault(cat, []).append(skill)
    return grouped


def home(request):
    projects = Project.objects.all()

    context = {
        'profile': get_profile(),
        'skills_by_category': grouped_skills(),

        'featured_projects': projects.filter(
            featured=True
        ),

        'experiences': Experience.objects.all()[:2],

        # Dynamic statistics
        'project_count': projects.count(),
        'experience_count': Experience.objects.count(),

        'active_page': 'home',
    }

    return render(
        request,
        'core/home.html',
        context
    )


def about(request):
    context = {
        'profile': get_profile(),
        'education': Education.objects.all(),
        'certifications': Certification.objects.all(),
        'active_page': 'about',
    }
    return render(request, 'core/about.html', context)


def skills(request):
    context = {
        'profile': get_profile(),
        'skills_by_category': grouped_skills(),
        'active_page': 'skills',
    }
    return render(request, 'core/skills.html', context)


def projects(request):
    context = {
        'profile': get_profile(),
        'projects': Project.objects.all(),
        'active_page': 'projects',
    }
    return render(request, 'core/projects.html', context)


def experience(request):
    context = {
        'profile': get_profile(),
        'experiences': Experience.objects.all(),
        'active_page': 'experience',
    }
    return render(request, 'core/experience.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        msg = request.POST.get('message', '')
        if name and email and subject and msg:
            Message.objects.create(name=name, email=email, subject=subject, message=msg)
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'status': 'ok'})
            messages.success(request, 'Message sent successfully! I will get back to you soon.')
            return redirect('core:contact')

    context = {
        'profile': get_profile(),
        'active_page': 'contact',
    }
    return render(request, 'core/contact.html', context)


def robots_txt(request):
    content = """User-agent: *
Allow: /

Disallow: /dashboard/
Disallow: /admin/

Sitemap: https://kaushal121.pythonanywhere.com/sitemap.xml
"""

    return HttpResponse(
        content,
        content_type="text/plain"
    )