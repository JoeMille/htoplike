from django.db import models
from django.utils import timezone

class SystemStats(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)

    cpu_percent = models.FloatField(null=True, blank=True)

    memory_total = models.BigIntegerField(null=True, blank=True)

    memory_available = models.BigIntegerField(null=True, blank=True)

    memory_percent = models.FloatField(null=True, blank=True)

    memory_used = models.BigIntegerField(null=True, blank=True)

    swap_total = models.BigIntegerField(null=True, blank=True)

    swap_used = models.BigIntegerField(null=True, blank=True)

    swap_percent = models.FloatField(null=True, blank=True)

    cpu_count = models.IntegerField(null=True, blank=True)

    cpu_count_logical = models.IntegerField(null=True, blank=True)

    load_average = models.CharField(max_length=100, null=True, blank=True)

    disk_total = models.BigIntegerField(null=True, blank=True)

    disk_used = models.BigIntegerField(null=True, blank=True)

    disk_free = models.BigIntegerField(null=True, blank=True)

    disk_percent = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'System Statistics'
        verbose_name_plural = 'System Statistics'
    
    def __str__(self):
        return f"System Stats - {self.timestamp}"