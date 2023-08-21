from django.db import models
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from django_prometheus.models import ExportModelOperationsMixin
from django.contrib.auth import models as AuthModels

# Local apps
from td_apps.core.models import BaseModel


class UserManager(AuthModels.BaseUserManager):
    def _create_user(self, email=None, password=None, **extra_fields):
        if email:
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
        else:
            raise ValueError("An Email must be given")
        user.set_password(password)
        user.full_clean()
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        try:
            user = get_user_model().objects.get(Q(email=email), is_active=False)
        except get_user_model().DoesNotExist:
            user = None

        if user:
            return user

        extra_fields.setdefault("is_active", False)
        extra_fields.setdefault("is_admin", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(email=email, password=password, **extra_fields)

    def create_admin(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email=email, password=password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email=email, password=password, **extra_fields)

class User(BaseModel, ExportModelOperationsMixin("User"),
           AuthModels.AbstractBaseUser, AuthModels.PermissionsMixin):
    """
    Custom Django User Model
    that extends AbstractBaseUser
    """
    profile_photo = models.ImageField(_("profile photo"), upload_to="users/images/",
                                      null=True, blank=True)
    first_name = models.CharField(_("first name"), max_length=100, null=True, blank=True)
    last_name = models.CharField(_("last name"), max_length=100, null=True, blank=True)
    email = models.EmailField(_("email"), validators=[EmailValidator],
                              unique=True, null=True, blank=True, db_index=1)
    is_active = models.BooleanField(_("is active"), default=False)
    is_superuser = models.BooleanField(_("is superuser"), default=False)
    is_admin = models.BooleanField(_("is admin"), default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email

    @property
    def is_staff(self):

        return self.is_admin

    @property
    def full_name(self):
        """
        Method for getting user's full name
        by combining first name and last name
        """
        return f"{self.first_name}, {self.last_name}"