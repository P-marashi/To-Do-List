"""you can  write pytest in terminal for test
 all of the api and serializer and models"""
import pytest
from django.contrib.auth import get_user_model
from td_apps.user.models import User

# Test case for creating a regular user
@pytest.mark.django_db
def test_create_user():
    # Test creating a user
    user = User.objects.create_user(email="test@example.com", password="password")
    assert user.email == "test@example.com"
    assert user.is_active == False

# Test case for creating an admin user
@pytest.mark.django_db
def test_create_admin():
    # Test creating an admin
    admin = User.objects.create_admin(email="admin@example.com", password="ad")
    assert admin.email == "admin@example.com"
    assert admin.is_admin == True

# Test case for creating a superuser
@pytest.mark.django_db
def test_create_superuser():
    # Test creating a superuser
    superuser = User.objects.create_superuser(email="superuser@example.com", password="1234")
    assert superuser.email == "superuser@example.com"
    assert superuser.is_superuser == True
