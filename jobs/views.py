from datetime import datetime as dt

from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from jobs.models import Job


def index(request):
    now = dt.now()
    open_jobs = Job.objects.filter(Q(deadline__gte=now.date()))
    expired_jobs = Job.objects.filter(Q(deadline__lt=now.date())).reverse()[:5]
    return render(
        request, "index.html", {"open_jobs": open_jobs, "expired_jobs": expired_jobs}
    )


def detail(request, job_id, **kwargs):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, "job.html", {"job": job})
