from django import forms
from core.models import Profile, Skill, Project, Experience, Education, Certification


def style_fields(form):
    for name, field in form.fields.items():
        widget = field.widget
        if isinstance(widget, (forms.CheckboxInput,)):
            widget.attrs.setdefault('class', 'dash-checkbox')
        elif isinstance(widget, (forms.Select,)):
            widget.attrs.setdefault('class', 'dash-select')
        else:
            widget.attrs.setdefault('class', 'dash-input')
    return form


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'title', 'bio', 'email', 'phone', 'location',
                  'github', 'linkedin', 'twitter', 'resume',
                  'years_experience', 'projects_count', 'clients_count']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 6}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields(self)


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'category', 'level', 'icon', 'order']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields(self)
        self.fields['icon'].help_text = "FontAwesome class, e.g. 'fab fa-python' (optional)"
        self.fields['level'].help_text = "Proficiency 0-100"


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'short_desc', 'description', 'tech_stack',
                  'github_url', 'live_url', 'featured', 'order', 'year']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'short_desc': forms.Textarea(attrs={'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields(self)
        self.fields['tech_stack'].help_text = "Comma-separated, e.g. 'Python, Django, PostgreSQL'"


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['role', 'company', 'description', 'start_date', 'end_date', 'current', 'location']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields(self)


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'detail', 'start_year', 'end_year']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields(self)


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['name', 'issuer', 'year']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields(self)
