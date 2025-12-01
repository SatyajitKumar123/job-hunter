from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import JobApplication
from .forms import JobForm


@login_required
def job_list(request):
    jobs = JobApplication.objects.filter(user=request.user)
    
    query = request.GET.get('q')
    if query:
        jobs = jobs.filter(
            Q(company__icontains=query) | Q(position__icontains=query)
        )
    return render(request, 'job_list.html', {'jobs': jobs})

@login_required
def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'job_form.html', {'form': form, 'title': 'Add Job'})

@login_required
def job_update(request, pk):
    job = get_object_or_404(JobApplication, pk=pk, user=request.user)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm(instance=job)
    return render(request, 'job_form.html', {'form': form, 'title': 'Edit Job'})

@login_required
def job_delete(request, pk):
    job = get_object_or_404(JobApplication, pk=pk, user=request.user)
    
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')
    return render(request, 'job_confirm_delete.html', {'job': job})