# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)


class Expense(TimeStampedModel):
    description = models.CharField(max_length=200)
    amount = models.CharField(max_length=100)
    date = models.DateField(max_length=8)
    catgory = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
