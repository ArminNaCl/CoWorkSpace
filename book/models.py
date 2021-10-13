import datetime

from django.db import models
from django.utils import timezone

from core.models import BaseModel, TimestampMixin
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class BookTable(BaseModel, TimestampMixin):
    id = models.AutoField(_('id'), primary_key=True, db_index=True, unique=True)
    user = models.ForeignKey('account.Profile', verbose_name=_('user'), on_delete=models.CASCADE,
                             related_name='book', related_query_name='books')
    table = models.ForeignKey('building.Table', verbose_name=_('table'), on_delete=models.CASCADE,
                              related_name='book', related_query_name='books')
    start_at = models.DateTimeField(_('start_at'), default=timezone.now)
    end_at = models.DateTimeField(_('end_at'))

    @property
    def days(self):
        return (self.end_at - self.start_at).days

    @property
    def price(self):
        return self.days*self.table.price_per_day

    def __str__(self):
        return f'{self.id}: {str(self.user)}-{str({self.table})}'

    class Meta:
        verbose_name = _('book table')
        verbose_name_plural = _('book tables')


class BookRoom(BaseModel, TimestampMixin):
    id = models.AutoField(_('id'), primary_key=True, db_index=True, unique=True)
    startUp = models.ForeignKey('account.StartUp', verbose_name=_('startUp'), on_delete=models.CASCADE,
                                related_name='book', related_query_name='books', )
    room = models.ForeignKey('building.Room', verbose_name=_('room'), on_delete=models.CASCADE,
                             related_name='book', related_query_name='books')
    start_at = models.DateTimeField(_('start at'), default=timezone.now)
    end_at = models.DateTimeField(_('end at'))

    @property
    def months(self):
        return (self.end_at.year - self.start_at.year)*12+(self.end_at.month-self.start_at.month)

    @property
    def price(self):
        return self.room.price_per_month*self.months

    def __str__(self):
        return f'{self.id}: {str(self.startUp)}-{str(self.room)}'

    class Meta:
        verbose_name = _('book room')
        verbose_name_plural = _('book rooms')
