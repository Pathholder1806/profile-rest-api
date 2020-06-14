from django.db import models
from django.contrib.auth.models import AbstractBaseUser   #Base for our user model
from django.contrib.auth.models import PermissionsMixin    #Controls permisiions granted to user
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps django to work with our custom user model."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""

        if not email:
            raise ValueError('The user must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new super user with given details."""

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    """These are the fields that are actually present in the inbuilt django 'user model'."""

    objects = UserProfileManager()  #This is also present in inbuilt django 'user model'.

    USERNAME_FIELD = 'email'   # We are using email instead of using name for User-Name.
    REQUIRED_FIELDS = ['name']   # List of fields that are required for every user.

    def get_full_name(self):
        """It is used to get a user's full name."""

        return self.name

    def get_short_name(self):
        """It is used to get a user's short name."""

        return self.name

    def __str__(self):
        """Django uses this when it needs to convert an object to string."""

        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update."""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns model as a string."""
        return self.status_text
