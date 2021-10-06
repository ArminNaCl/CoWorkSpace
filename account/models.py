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
    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE, related_name='user_of')
    first_name = models.CharField(_('First name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=100)

    def start_up(self):
        return StartUpMembers.objects.filter(member=self).first()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'


class StartUp(BaseModel, TimestampMixin):
    id = models.AutoField(_('id'), primary_key=True, db_index=True, unique=True, )
    header = models.OneToOneField(User, verbose_name=_('header'), on_delete=models.CASCADE, related_name='header_of')
    name = models.CharField(_('name'), max_length=120)
    website = models.URLField(_('website'), )
    description = models.TextField(_('description'), )

    def members(self):
        return StartUpMembers.objects.filter(startUp=self).member

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'startUp'
        verbose_name_plural = 'startUps'


class StartUpMembers(BaseModel, TimestampMixin):
    id = models.AutoField(_('id'), primary_key=True, db_index=True, unique=True, )
    member = models.ForeignKey('account.User', verbose_name=_('member'), on_delete=models.CASCADE,
                               related_name='member', related_query_name='members')
    startUp = models.ForeignKey('account.StartUp', verbose_name=_('startUp'), on_delete=models.CASCADE,
                                related_name='member', related_query_name='members',)
    job_title = models.CharField(_('job title'), max_length=120, db_index=True)

    def __str__(self):
        return f'{self.id}: {str(self.startUp)}-{str(self.job_title)}'

    class Meta:
        verbose_name = _('startup member')
        verbose_name_plural = _('startup members')