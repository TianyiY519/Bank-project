
from __future__ import absolute_import, unicode_literals
from celery import Task

from UserAdmin.models import User
from .models import Interest


@Task(name="count_interest")
def count():
    users = User.objects.filter(account__balance__isnull=False)

    if users.exists():
        for user in users:
            balance = user.balance
            # calculates users interest
            amount = (balance * 10) / 100
            Interest.objects.create(user=user, amount=amount)
            # adds users interest to balance.
            user.account.balance += amount
            user.account.save()