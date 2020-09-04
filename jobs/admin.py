from django.contrib import admin

from jobs.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        "time",
        "user",
        "info_by",
        "company_name",
        "paid",
        "position_name",
        "deadline",
    ]
    list_filter = (
        "user",
        "platform",
        "job_type",
    )
    search_fields = (
        "company_name",
        "position_name",
    )
