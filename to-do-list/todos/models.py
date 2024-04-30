from django.db import models


class Todo(models.Model):
    title = models.CharField(verbose_name="Tutulo", max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline_at = models.DateTimeField(verbose_name="Prazo", null=False, blank=False)
    finished_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ["deadline_at"]
