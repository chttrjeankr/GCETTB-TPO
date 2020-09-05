from datetime import datetime as dt

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from jobs.choices import JOB_TYPES, PLATFORM_CHOICES


class Job(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    info_by = models.CharField(
        max_length=60, blank=True, verbose_name="Source (Person Name)"
    )
    company_name = models.CharField(max_length=100)
    position_name = models.CharField(max_length=100)
    paid = models.BooleanField(null=True, blank=True)
    job_type = models.CharField(max_length=2, choices=JOB_TYPES)
    desc_url = models.URLField(verbose_name="Description URL")
    appln_url = models.URLField(verbose_name="Application URL")
    deadline = models.DateField(null=True, blank=True, verbose_name="Deadline (if any)")
    job_open = models.BooleanField(
        default=True, blank=True, verbose_name="Is this job open?"
    )
    platform = models.CharField(max_length=4, choices=PLATFORM_CHOICES)
    remarks = models.TextField(default="No Remarks")

    @property
    def is_job_open(self):
        if self.deadline:
            date_today = dt.today().date()
            return self.deadline >= date_today
        else:
            return self.job_open

    def clean(self):
        if self.deadline is None and self.job_open is None:
            raise ValidationError("Has to have a open/closed status")
        if self.deadline:
            self.job_open = self.is_job_open

    def save(self, *args, **kwargs):
        if not self.info_by:
            self.info_by = self.user.get_full_name()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.company_name}: {self.position_name}"

    class Meta:
        ordering = ["deadline", "company_name", "position_name"]
