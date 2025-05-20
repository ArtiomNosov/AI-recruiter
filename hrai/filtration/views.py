from django.shortcuts import render
from django.http import HttpResponse


from django.shortcuts import render
from .models import Resume
from .forms import ResumeFilterForm


def candidate_list(request):
    resumes = Resume.objects.all()
    form = ResumeFilterForm(request.GET or None)

    if form.is_valid():
        skills = form.cleaned_data.get('skills')
        experience = form.cleaned_data.get('experience')
        desired_salary = form.cleaned_data.get('desired_salary')

        if skills:
            skills_list = [skill.strip().lower() for skill in skills.split(',')]
            for skill in skills_list:
                resumes = resumes.filter(skills__icontains=skill)

        if experience:
            resumes = resumes.filter(experience=experience)

        if desired_salary:
            resumes = resumes.filter(desired_salary=desired_salary)

    return render(request, 'main/includes/candidate_list.html', {
        'resumes': resumes,
        'form': form
    })