from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, creditcard


class UserBaseForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {'first_name': 'First name', 'last_name': 'Last Name', 'email': 'Email'}


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('is_user', 'is_manager', 'account')
        labels = {'is_user': 'User', 'is_manager': 'Manager'}

class UserCreditcardForm(forms.ModelForm):
    class Meta:
        model = creditcard
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     self.Username = kwargs.pop('Username')
    #     super().__init__(*args, **kwargs)

    # def save(self, commit=True):
    #     self.instance.SSN = self.SSN
    #     # self.instance.balance_after_transaction = self.account.balance
    #     return super().save()

    # def __init__(self, user, *args, **kwargs):
    #     super(UserCreditcardForm, self).__init__(*args, **kwargs)
    #
    #     self.fields['Username'] = forms.ModelChoiceField(queryset=UserProfile.objects.filter(Username=user))

# class UserCreditcardForm(forms.ModelForm):
#     def __init__(self, user, * args, ** kwargs):
#         super(UserCreditcardForm, self).__init__(*args, **kwargs)
#         self.fields['enrolled_course'] = forms.ModelChoiceField(queryset=UserProfile.objects.filter(student=user))
#
#     class Meta:
#         model = creditcard
#         fields = "__all__"