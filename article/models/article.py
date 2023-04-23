from django.db import models
from commons.models.abstract_date_time import AbstractModelWithTimeStamps
from user.models.user import User


class Article(AbstractModelWithTimeStamps):
    title = models.CharField(max_length=100)
    banner = models.ImageField(upload_to="banners/",null=True,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.id} || {self.title}"
