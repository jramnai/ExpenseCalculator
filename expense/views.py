# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.db.models import Sum
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Expense

# Create your views here.


def index(request):
    """
    """
    total_expense = Expense.objects.aggregate(Sum('amount'))
    return render(
        request,
        'expense/index.html',
        {
            'total_expense': total_expense['amount__sum']
        }
    )


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
