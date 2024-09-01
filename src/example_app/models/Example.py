from django.db import models


class Example(models.Model):

    title = models.CharField(max_length=255)

    def __str__(self):

        return self.title

    class Meta:

        verbose_name = "Example"
        verbose_name_plural = "Examples"
