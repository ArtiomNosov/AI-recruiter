from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView
from .forms import ResumeUploadForm
from .models import Resume

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Resume
from .forms import ResumeUploadForm
class ResumeUploadView(LoginRequiredMixin, FormView):
    
    template_name = 'download/upload.html'
    form_class    = ResumeUploadForm
    success_url   = reverse_lazy('resume_tools')

    def form_valid(self, form):
        resume = form.save(commit=False)
        resume.user = self.request.user
        resume.save()
        # сохраняем и отсылаем на панель инструментов
        return super().form_valid(form)

class ResumeToolsView(LoginRequiredMixin, ListView):
    model = Resume
    template_name = 'download/tools.html'
    context_object_name = 'resumes'

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)


class ResumeDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        resume = get_object_or_404(Resume, pk=pk, user=request.user)
        resume.file.delete(save=False)  # удаляем файл из media/
        resume.delete()
        messages.success(request, "Резюме удалено.")
        return redirect('resume_tools')