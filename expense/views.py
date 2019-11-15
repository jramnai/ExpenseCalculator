# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Sum
from django.shortcuts import render
from .models import Expense

# Create your views here.
def index(request):
	"""
	"""
	total_expense = Expense.objects.aggregate(Sum('amount'))
	return render(request, 'expense/index.html', {'total_expense': total_expense['amount__sum']})