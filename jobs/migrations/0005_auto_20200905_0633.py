# Generated by Django 3.0.8 on 2020-09-05 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20200905_0616'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['deadline', 'company_name', 'position_name']},
        ),
    ]
