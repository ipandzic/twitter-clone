from django.conf import settings
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db import models


def validate_content(value):
    content = value
    if content == "abc":
        raise ValidationError("Content Cannot be ABC")
    return value


class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-timestamp"]


    # def clean(self, *args, **kwargs):
    #     content = self.content
    #     if content == "abc":
    #         raise ValidationError("Content Cannot be ABC")
    #     return super(Tweet, self).clean(*args, **kwargs)
