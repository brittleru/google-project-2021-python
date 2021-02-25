from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
# from accounts.models import User
from django.contrib.auth import get_user_model
from django import template
import misaka


User = get_user_model()
register = template.Library()


class Forum(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through="ForumMember")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("forums:single", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["name"]


class ForumMember(models.Model):
    forum = models.ForeignKey(Forum, related_name="memberships", on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, related_name='user_forums', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("forum", "user")
