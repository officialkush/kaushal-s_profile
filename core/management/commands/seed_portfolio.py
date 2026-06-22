from django.core.management.base import BaseCommand
from datetime import date
from core.models import Profile, Skill, Project, Experience, Education, Certification


class Command(BaseCommand):
    help = "Seed the database with Kaushal Kumar's portfolio data"

    def handle(self, *args, **options):
        # ---------------- Profile ----------------
        Profile.objects.all().delete()
        Profile.objects.create(
            name="Kaushal Kumar",
            title="GenAI / Python Developer",
            bio=(
                "GenAI / Python Developer with hands-on experience in Machine Learning, "
                "AI-powered applications, backend development, and cloud deployment. "
                "Skilled in Python, Flask, Django, Scikit-Learn, REST APIs, and Generative AI "
                "technologies. Experienced in building and deploying end-to-end ML solutions "
                "and scalable web applications."
            ),
            email="kaushalraj11a@gmail.com",
            phone="+91-6206476736",
            location="Patna, India",
            github="https://github.com/officialkush",
            linkedin="https://linkedin.com/in/kaushalkumar0",
            years_experience="1+",
            projects_count=15,
            clients_count=1,
        )

        # ---------------- Skills ----------------
        Skill.objects.all().delete()
        skills = [
            # AI / ML
            ("Machine Learning", 90, "ai_ml", "fas fa-brain", 1),
            ("Deep Learning", 80, "ai_ml", "fas fa-network-wired", 2),
            ("PyTorch", 75, "ai_ml", "fas fa-fire", 3),
            ("TensorFlow", 75, "ai_ml", "fas fa-project-diagram", 4),
            ("NLP", 80, "ai_ml", "fas fa-comment-dots", 5),
            ("RAG", 88, "ai_ml", "fas fa-database", 6),
            ("Prompt Engineering", 88, "ai_ml", "fas fa-magic", 7),
            ("LangChain", 82, "ai_ml", "fas fa-link", 8),
            # Backend
            ("Python", 92, "backend", "fab fa-python", 1),
            ("Django", 90, "backend", "fas fa-server", 2),
            ("Flask", 85, "backend", "fas fa-flask", 3),
            ("FastAPI", 75, "backend", "fas fa-bolt", 4),
            ("REST API Design", 88, "backend", "fas fa-plug", 5),
            # Frontend
            ("HTML / CSS", 85, "frontend", "fab fa-html5", 1),
            ("JavaScript", 78, "frontend", "fab fa-js", 2),
            ("Django Templates", 88, "frontend", "fas fa-code", 3),
            # Databases
            ("PostgreSQL", 82, "database", "fas fa-database", 1),
            ("MySQL", 80, "database", "fas fa-database", 2),
            ("SQLite", 85, "database", "fas fa-database", 3),
            # Cloud & DevOps
            ("AWS (EC2, S3, IAM)", 78, "cloud", "fab fa-aws", 1),
            ("Docker", 75, "cloud", "fab fa-docker", 2),
            ("Git / GitHub", 88, "cloud", "fab fa-github", 3),
            ("Postman", 85, "cloud", "fas fa-paper-plane", 4),
            ("Netlify / Render", 80, "cloud", "fas fa-cloud", 5),
        ]
        for name, level, cat, icon, order in skills:
            Skill.objects.create(name=name, level=level, category=cat, icon=icon, order=order)

        # ---------------- Projects ----------------
        Project.objects.all().delete()
        Project.objects.create(
            title="JanMitra AI — जनमित्र AI",
            short_desc="AI-powered citizen assistance platform for government schemes & public services.",
            description=(
                "Developed an AI-powered citizen assistance platform providing guidance on "
                "government schemes, document requirements, and public services. Implemented a "
                "Retrieval-Augmented Generation (RAG) pipeline to deliver contextual and accurate "
                "responses from curated knowledge sources. Integrated Gemini API with prompt "
                "engineering techniques to generate multilingual responses and personalized "
                "recommendations. Built scalable backend APIs and data-processing workflows using "
                "Django and PostgreSQL, with a responsive real-time chat interface."
            ),
            tech_stack="Python, Django, Gemini API, RAG, PostgreSQL, HTML, CSS, JavaScript",
            featured=True,
            order=1,
            year="2026",
        )
        Project.objects.create(
            title="Medical Insurance Cost Prediction",
            short_desc="ML web app predicting insurance costs with an R² score of 0.97.",
            description=(
                "Developed and deployed a machine learning web application to predict medical "
                "insurance costs based on age, BMI, smoking status, gender, region, and dependents. "
                "Performed data preprocessing, feature encoding, and model training, integrating the "
                "trained regression model into a Flask application — achieving an R² score of 0.97 "
                "on a test dataset of 2700+ rows. Deployed on Render for real-time predictions."
            ),
            tech_stack="Python, Scikit-Learn, Flask, HTML, CSS, Render",
            github_url="https://github.com/officialkush/medical-insurance-cost-prediction",
            live_url="https://medical-insurance-cost-prediction-y255.onrender.com",
            featured=True,
            order=2,
            year="2026",
        )
        Project.objects.create(
            title="AI Weather Dashboard",
            short_desc="Real-time weather dashboard with AI-generated insights and Chart.js visuals.",
            description=(
                "Developed an AI-powered weather dashboard that displays real-time weather data and "
                "forecasts by integrating live Weather APIs. Integrated Gemini API to generate "
                "contextual weather insights and activity recommendations based on forecast data. "
                "Built interactive UI components including temperature charts, forecast grids, and "
                "weather maps using JavaScript and Chart.js."
            ),
            tech_stack="Python, Django, REST APIs, HTML, CSS, JavaScript, Chart.js",
            featured=False,
            order=3,
            year="Oct – Dec 2025",
        )

        # ---------------- Experience ----------------
        Experience.objects.all().delete()
        Experience.objects.create(
            company="Petpooja (Prayosha Food Services)",
            role="Software Engineer",
            description=(
                "B2B SaaS platform serving 50,000+ restaurants. Tested and validated workflows for "
                "the 'Tasks' product, ensuring smooth functionality and a reliable user experience "
                "across edge cases. Built responsive client-facing web pages using HTML, CSS, "
                "JavaScript, and Django templates, improving frontend delivery speed. Deployed and "
                "managed client-facing webpages on Netlify and GoDaddy, gaining hands-on cloud and "
                "web deployment experience."
            ),
            start_date=date(2025, 5, 1),
            end_date=date(2026, 4, 30),
            current=False,
            location="Patna, India",
        )
        Experience.objects.create(
            company="TNS India Foundation",
            role="Full Stack Developer Intern",
            description=(
                "Developed backend logic and REST-style API services for an e-commerce management "
                "platform handling product and order workflows. Implemented SQL-based CRUD operations "
                "and authentication-ready backend flows to support secure user interactions. "
                "Integrated frontend interfaces with backend APIs, ensuring accurate data exchange "
                "and transaction handling across modules."
            ),
            start_date=date(2024, 3, 1),
            end_date=date(2024, 5, 31),
            current=False,
            location="India",
        )

        # ---------------- Education ----------------
        Education.objects.all().delete()
        Education.objects.create(
            institution="Excel Engineering College, Anna University Chennai",
            degree="B.Tech — Information Technology",
            detail="Best Outgoing Student – IT",
            start_year="2021",
            end_year="2025",
        )

        # ---------------- Certifications ----------------
        Certification.objects.all().delete()
        Certification.objects.create(name="Machine Learning", issuer="Simplilearn", year="")
        Certification.objects.create(
            name="Machine Learning A-Z: AI, Machine Learning, Deep Learning, AWS, Python & R",
            issuer="Udemy", year="2026"
        )
        Certification.objects.create(
            name="Introduction to Generative AI Studio", issuer="Simplilearn", year=""
        )

        self.stdout.write(self.style.SUCCESS("Portfolio data seeded successfully for Kaushal Kumar."))
