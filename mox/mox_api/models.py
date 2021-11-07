from django.db import models


class Link(models.Model):
    url = models.URLField(max_length=500)
    # updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.url[0:100]
