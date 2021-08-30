from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from core.managers import BaseManager


# Create your models here.

class TimestampMixin(models.Model):
    create_time = models.DateTimeField(_('create timestamp'), auto_now_add=True)
    update_time = models.DateTimeField(_('update timestamp'), auto_now=True)

    class Meta:
        abstract = True


class BaseModel(models.Model):
    """
    Base Model with Logical Delete(Archiving)
    """

    class Meta:
        abstract = True

    objects = BaseManager()

    deleted = models.BooleanField(default=False, db_index=True)
    delete_time = models.DateTimeField(_('delete time'), default=None, null=True, blank=True)

    def delete(self):
        self.deleted = True
        self.delete_time = timezone.now()
        self.save()


class TestModel(BaseModel):
    """
    BaseModel is abstract so TestModel is a class for tests
    """
    pass
