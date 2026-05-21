from django.shortcuts import render
from .models import Skill, Experience, Education, ContactLink


def home(request):
    skills = Skill.objects.all()

    experiences = (
        Experience.objects
        .prefetch_related("points", "links")
        .all()
    )

    educations = Education.objects.all()
    contact_links = ContactLink.objects.all()

    context = {
        "skills": skills,
        "experiences": experiences,
        "educations": educations,
        "contact_links": contact_links,
    }

    return render(request, "portofolio/index.html", context)