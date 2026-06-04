from django.db import migrations
from django.contrib.auth.models import User
import os

def create_superuser(apps, schema_editor):
    # This checks if the user exists so it doesn't try to create it twice
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='your-email@example.com',
            password='yourpassword' # Choose a secure password
        )

class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'), # Ensure this matches your previous migration file name
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]