from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    class Meta:
        db_table = 'user_profile'
        verbose_name = 'user_profile'
        verbose_name_plural = 'User Profile'

    @property
    def balance(self):
        if hasattr(self, 'account'):
            return self.account.balance
        return 0
    account = models.CharField(max_length=500)
    is_user = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)
    # profile_image = models.ImageField(upload_to='profile/%Y/%m/%d', verbose_name='Profile Image',
    #                                   name="profile_image", null=True)
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE,
    )
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )
    interest_start_date = models.DateField(
        null=True, blank=True,
        help_text=(
            'The month number that interest calculation will start from'
        )
    )
    initial_deposit_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.profile.save()

class creditcard(models.Model):
    Username = models.OneToOneField(
        User,
        related_name='creditcard',
        on_delete=models.DO_NOTHING,
    )

    # account = models.ForeignKey(
    #     UserProfile,
    #     related_name='transactions',
    #     on_delete=models.DO_NOTHING,
    # )

    SSN = models.DecimalField(
        max_digits=9,
        decimal_places=0
    )

    income = models.DecimalField(
        max_digits=20,
        decimal_places=2
    )

    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
    )

    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
    )

    city = models.CharField(
        "City",
        max_length=1024,
    )

    objects = models.Manager()