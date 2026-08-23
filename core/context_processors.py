from .models import Profile, Skill


def seo_data(request):
    profile = Profile.objects.first()

    skills = Skill.objects.all().order_by(
        "order",
        "name"
    )

    return {
        "seo_profile": profile,
        "seo_skills": skills,
    }