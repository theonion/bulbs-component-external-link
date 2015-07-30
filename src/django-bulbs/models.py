from django.db import models


class ExternalLinkMixin(models.Model):
    """This content just links to an external URL."""

    url = models.URLField(null=True, blank=True)

    class Meta:
        abstract = True

    def get_absolute_url(self):
        return self.url
