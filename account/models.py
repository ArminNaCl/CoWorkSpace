from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import TimestampMixin, BaseModel


class User(AbstractBaseUser, TimestampMixin):
    id = models.AutoField(_('id'), primary_key=True, db_index=True, unique=True, )
    username = models.CharField(_('username'), unique=True, max_length=40)
    email = models.EmailField(_('Email Address'), unique=True, max_length=100)
    is_admin = models.BooleanField(_('Is Admin'), default=False)
    is_active = models.BooleanField(_('Is Active'), default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Profile(BaseModel):
    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE)

