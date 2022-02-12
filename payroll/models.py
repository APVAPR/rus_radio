from django.conf import settings
from django.db import models


class Timesheet(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Сотрудник')
    total_hours = models.IntegerField(verbose_name='Всего отработанных часов')
    period = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Период')

    def __str__(self):
        return f'{self.user_id}: {self.total_hours}'

    class Meta:
        verbose_name = 'Табель'
        verbose_name_plural = 'Табель'