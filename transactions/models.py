from django.db import models
from django.conf import settings
from UserAdmin.models import UserProfile

class Transaction(models.Model):
    DEPOSIT = 1
    WITHDRAWAL = 2
    INTEREST = 3

    TRANSACTION_TYPE_CHOICES = (
        (DEPOSIT, 'Deposit'),
        (WITHDRAWAL, 'Withdrawal'),
        (INTEREST, 'Interest'),
    )

    account = models.ForeignKey(
        UserProfile,
        related_name='transactions',
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    balance_after_transaction = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    transaction_type = models.PositiveSmallIntegerField(
        choices=TRANSACTION_TYPE_CHOICES
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.account.account_no)

    class Meta:
        ordering = ['timestamp']

class Interest(models.Model):
    User = settings.AUTH_USER_MODEL

    user = models.ForeignKey(
        User,
        related_name='interests',
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)