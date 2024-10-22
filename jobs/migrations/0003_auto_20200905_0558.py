# Generated by Django 3.0.8 on 2020-09-05 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20200904_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_open',
            field=models.BooleanField(blank=True, default=True, verbose_name='Is this job open?'),
        ),
        migrations.AlterField(
            model_name='job',
            name='deadline',
            field=models.DateField(blank=True, null=True, verbose_name='Deadline (if any)'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('IT', 'Internship'), ('EC', 'Exam/Competition'), ('FT', 'Full Time Job')], max_length=2),
        ),
        migrations.AlterField(
            model_name='job',
            name='platform',
            field=models.CharField(choices=[('YOUT', 'YouTube'), ('CMPY', 'Company Page'), ('LNKD', 'LinkedIn'), ('OTHR', 'Others'), ('INTS', 'Internshala')], max_length=4),
        ),
    ]
