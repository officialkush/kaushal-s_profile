from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    photo = models.ImageField(upload_to='profile/', blank=True, null=True) 
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=100, blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    resume = models.FileField(upload_to='resume/', blank=True)
    years_experience = models.CharField(max_length=20, default="1+")
    projects_count = models.IntegerField(default=0)
    clients_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('ai_ml', 'AI / ML'),
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('database', 'Databases'),
        ('cloud', 'Cloud & DevOps'),
    ]
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=80)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='backend')
    icon = models.CharField(max_length=50, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_desc = models.CharField(max_length=300, blank=True)
    tech_stack = models.CharField(max_length=300)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    year = models.CharField(max_length=20, blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',')]


class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    location = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.role} @ {self.company}"


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    detail = models.CharField(max_length=300, blank=True)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10)

    class Meta:
        ordering = ['-start_year']

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=150, blank=True)
    year = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"
