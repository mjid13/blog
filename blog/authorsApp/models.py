from django.db import models

from django.contrib.auth.models import User

def validate_image_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # Get the file extension
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']  # List of valid extensions
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
            upload_to='media/profile',
            default='media/default_profile.png',
            blank=True,
            null=True,
            validators=[validate_image_file_extension]
    )
    bio = models.TextField(max_length=500, blank=True, help_text="Tell us a little bit about yourself.", null=True)
    rule = models.TextField(max_length=500, blank=True, null=True)
    email = models.TextField(max_length=500, blank=True)
    last_login = models.DateTimeField(max_length=500, blank=True, null=True)
    regestred_at = models.DateTimeField(max_length=500, blank=True, null=True)
    github = models.TextField(max_length=500, blank=True, null=True)
    linkedin = models.TextField(max_length=500, blank=True, null=True)
    website = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateTimeField(null=True, blank=True)




    def __str__(self):
        return self.user

