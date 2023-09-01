# Generated by Django 4.1.4 on 2023-09-01 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('bio', models.TextField(blank=True, max_length=2000, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.CharField(choices=[('PATIENT', 'P'), ('DOCTOR', 'D')], default=('PATIENT', 'P'), max_length=8)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
