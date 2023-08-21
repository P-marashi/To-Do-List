from django.db import models
from django.utils.translation import gettext_lazy as _


# Abstract base model to provide common fields for other models
class BaseModel(models.Model):
    """
    Abstract Base Model for the project.

    Attributes:
        created_at: DateTimeField(auto_now_add=True)
        updated_at: DateTimeField(auto_now=True)
    """
    
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        abstract = True
