from django.contrib.postgres.fields import JSONField
from django.db import models


class DomeinData(models.Model):
    data = JSONField()

    class Meta:
        verbose_name = 'domeindata'
        verbose_name_plural = 'domeindata'

    def __str__(self) -> str:
        if isinstance(self.data, dict):
            return str(list(self.data.keys))[:50]
        return str(self.data)[:50]
