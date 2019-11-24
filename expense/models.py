# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from model_utils.models import TimeStampedModel

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def get_total_cost(self):
        return sum(item for item in self.items.all())

    def __str__(self):
        return self.name


class Expense(models.Model):

    description = models.CharField(max_length=200)
    amount = models.CharField(max_length=100)
    date = models.DateField(max_length=8)
    catgory = models.ForeignKey(
        Category, related_name='items', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.description
