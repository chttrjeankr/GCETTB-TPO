from django.shortcuts import get_object_or_404, render

from jobs.models import Job


def index(request):
    all_jobs = Job.objects.all()
    open_jobs = [job for job in all_jobs if job.is_job_open]
    expired_jobs = [job for job in all_jobs.reverse() if not job.is_job_open][:5]
    return render(
        request, "index.html", {"open_jobs": open_jobs, "expired_jobs": expired_jobs}
    )


def detail(request, job_id, **kwargs):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, "job.html", {"job": job})
