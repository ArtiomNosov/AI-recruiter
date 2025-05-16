from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from download.models import Resume, Vacancy
from download.forms import ResumeUploadForm
import mimetypes
from urllib.parse import quote
from .utils import extract_text_from_file 



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
    resume = get_object_or_404(Resume, pk=resume_id)
    file_ext = resume.file.name.split('.')[-1].lower() if resume.file.name else None
    
    # Извлекаем текст только для PDF
    text_content = extract_text_from_file(resume.file.path) if file_ext == 'pdf' else None
    
    # Формируем URL для Google Docs
    google_docs_url = None
    if file_ext in ['doc', 'docx']:
        file_url = request.build_absolute_uri(resume.file.url)
        google_docs_url = f"https://docs.google.com/viewer?url={quote(file_url)}&embedded=true"
    
    return render(request, 'view_resume/resume_detail.html', {
        'resume': resume,
        'file_ext': file_ext,
        'text_content': text_content,
        'google_docs_url': google_docs_url,
        'file_url': resume.file.url
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
    action = request.GET.get('action')
    
    if action == 'like':
        resume.likes.add(request.user)
    elif action == 'dislike':
        resume.likes.remove(request.user)
    
    return redirect('view_resume', pk=resume_id)


@login_required
@require_POST
def save_resume(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)
    # Здесь должна быть логика сохранения резюме для пользователя
    return JsonResponse({'status': 'success', 'action': 'save'})