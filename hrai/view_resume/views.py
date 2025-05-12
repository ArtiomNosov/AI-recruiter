from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from download.models import Resume, Vacancy
from download.forms import ResumeUploadForm

@login_required
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            file_ext = resume.file.name.split('.')[-1].lower()
            resume.fmt = 'pdf' if file_ext == 'pdf' else 'doc'
            resume.save()
            return redirect('resume_detail', resume_id=resume.id)
    else:
        form = ResumeUploadForm()
    
    return render(request, 'view_resume/upload_resume.html', {'form': form})

def resume_detail(request, resume_id):
    resume = get_object_or_404(Resume.objects.select_related('user', 'vacancy'), pk=resume_id)
    return render(request, 'view_resume/resume_detail.html', {
        'resume': resume,
        'file_url': resume.file.url if resume.file else None
    })

def resume_list(request):
    resumes = Resume.objects.select_related('user', 'vacancy').order_by('-uploaded_at')
    vacancies = Vacancy.objects.all()
    return render(request, 'view_resume/resume_list.html', {
        'resumes': resumes,
        'vacancies': vacancies
    })

@login_required
@require_POST
def like_resume(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)
    resume.likes += 1
    resume.save()
    return JsonResponse({'status': 'success', 'likes': resume.likes})

@login_required
@require_POST
def dislike_resume(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)
    resume.dislikes += 1
    resume.save()
    return JsonResponse({'status': 'success', 'dislikes': resume.dislikes})

@login_required
@require_POST
def save_resume(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)
    # Здесь должна быть логика сохранения резюме для пользователя
    return JsonResponse({'status': 'success', 'action': 'save'})