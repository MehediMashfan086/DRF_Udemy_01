import pytest
from django.test import TestCase

from django.contrib.auth.models import User

def test_should_create_user_with_username(db) -> None:
    user = User.objects.create_user("admin")
    assert user.username == "admin"
