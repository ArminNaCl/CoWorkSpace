from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from core.models import BaseModel, TimestampMixin


class Building(BaseModel, TimestampMixin):
    id = models.AutoField(_('id'), primary_key=True, db_index=True, unique=True, )
    name = models.CharField(_('Name'), max_length=120)
    street = models.CharField(_('Street'), max_length=120)
    post_code = models.PositiveBigIntegerField(_('Post Code'))

    def __str__(self):
        return self.name

    @property
    def count_tables(self):
        return self.tables.count()

    @property
    def count_rooms(self):
        return self.rooms.count()

    class Meta:
        verbose_name = 'building'
        verbose_name_plural = 'buildings'


class Table(BaseModel, TimestampMixin):
    id = models.AutoField(_('id'), primary_key=True, db_index=True, unique=True, )
    building = models.ForeignKey('Building', verbose_name=_('building'), on_delete=models.CASCADE,
                                 related_name='table', related_query_name='tables')
    capacity = models.PositiveSmallIntegerField(_('capacity'), default=1)
    price_per_hour = models.DecimalField(_('Price per Hours'), )

    def __str__(self):
        return str(self.building) + '-table-' + str(self.id)

    class Meta:
        verbose_name = 'table'
        verbose_name_plural = 'tables'


class Room(BaseModel, TimestampMixin):
    id = models.AutoField(_('id'), primary_key=True, db_index=True, unique=True, )
    building = models.ForeignKey('Building', verbose_name=_('building'), on_delete=models.CASCADE,
                                 related_name='room', related_query_name='rooms')
    capacity = models.PositiveSmallIntegerField(_('capacity'), default=6)
    has_tv = models.BooleanField(_('has TV'), default=False)
    has_printer = models.BooleanField(_('has TV'), default=False)
    price_per_day = models.DecimalField(_('price per day'))

    def __str__(self):
        return str(self.building) + '-room-' + str(self.id)

    class Meta:
        verbose_name = 'room'
        verbose_name_plural = 'rooms'
