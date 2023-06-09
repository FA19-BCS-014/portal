# Generated by Django 4.0.4 on 2023-05-21 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0002_job_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('phone', models.CharField(blank=True, max_length=1000, null=True)),
                ('address', models.CharField(blank=True, max_length=2000, null=True)),
                ('msg', models.CharField(blank=True, max_length=2000, null=True)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_applications', to='job.job')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_applications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'application',
            },
        ),
    ]
