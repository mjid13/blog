# Generated by Django 5.0.2 on 2024-02-20 14:15

import authorsApp.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='media/default_profile.png', null=True, upload_to='media/profile', validators=[authorsApp.models.validate_image_file_extension])),
                ('bio', models.TextField(blank=True, help_text='Tell us a little bit about yourself.', max_length=500)),
                ('rule', models.TextField(blank=True, max_length=500)),
                ('email', models.TextField(blank=True, max_length=500)),
                ('last_login', models.DateTimeField(blank=True, max_length=500)),
                ('regestred_at', models.DateTimeField(blank=True, max_length=500)),
                ('github', models.TextField(blank=True, max_length=500)),
                ('linkedin', models.TextField(blank=True, max_length=500)),
                ('website', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]