from django.conf import settings
from django.db import models

from jobs.choices import *


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
    deadline = models.DateField()
    platform = models.CharField(max_length=4, choices=PLATFORM_CHOICES)
    remarks = models.TextField(default="No Remarks")

    def save(self, *args, **kwargs):
        if not self.info_by:
            self.info_by = self.user.get_full_name()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.company_name}: {self.position_name}"

    class Meta:
        ordering = ["deadline"]
