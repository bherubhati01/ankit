import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')  # Change 'core' to your project name
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = "admin"
email = "admin@example.com"
password = "adminpass"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superuser created successfully.")
else:
    print("Superuser already exists.")
