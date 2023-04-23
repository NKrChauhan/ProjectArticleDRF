from django.db import models


class AbstractModelWithTimeStamps(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True)
