from django.forms import ModelForm

from jobs.models import Job


class JobForm(ModelForm):
    class Meta:
        model = Job
