import uuid
from django.db import models


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nconst = models.CharField(max_length=10, unique=True)
    primary_name = models.CharField(max_length=255, null=True, blank=True)
    birth_year = models.IntegerField(null=True, blank=True)
    death_year = models.IntegerField(null=True, blank=True)
    primary_profession = models.CharField(max_length=255, null=True, blank=True)
    known_for_titles = models.ManyToManyField('Title', related_name='persons', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.primary_name if self.primary_name else 'no primary name'

    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name = "Person"
        verbose_name_plural = "Persons"


class Title(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tconst = models.CharField(max_length=10, unique=True)
    title_type = models.CharField(max_length=50, null=True, blank=True)
    primary_title = models.CharField(max_length=255, null=True, blank=True)
    original_title = models.CharField(max_length=255, null=True, blank=True)
    is_adult = models.BooleanField(null=True, blank=True)
    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)
    runtime_minutes = models.IntegerField(null=True, blank=True)
    genres = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.primary_title if self.primary_title else 'no primary title'

    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name = "Title"
        verbose_name_plural = "Titles"
