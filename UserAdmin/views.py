from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .forms import UserBaseForm, UserProfileForm, UserCreditcardForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.db import transaction


# Create your views here.
def register_new_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse("Now you can log-in")  # this is a placeholder at present
            return HttpResponseRedirect(reverse("UserAdmin:userdamin_login"))
    elif request.method == "GET":
        form = UserCreationForm()
    return render(request, 'UserAdmin/register_new_user.html', context={'form': form})

@login_required
@transaction.atomic
def update_user_profile(request):
    user_instance = User.objects.get(id=request.user.id)
    profile_instance = UserProfile.objects.get(user_id=request.user.id)

    if request.method == 'POST':
        user_form = UserBaseForm(request.POST, instance=user_instance)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile_instance) # Change here

        if user_form.is_valid() and profile_form.is_valid():
            if user_form.has_changed() or profile_form.has_changed():
                user_instance.profile.account = profile_form.instance.account
                user_instance.profile.is_user = profile_form.instance.is_user
                user_instance.profile.is_manager = profile_form.instance.is_manager
                # if request.FILES.get('profile_image'):
                #     user_instance.profile.profile_image = request.FILES.get('profile_image') # Change here
                user_form.save()
            return HttpResponseRedirect(reverse("transactions:transaction_report"))

    elif request.method == 'GET':
        user_form = UserBaseForm(instance=user_instance)
        profile_form = UserProfileForm(instance=profile_instance)
    return render(request, 'useradmin/update_user_profile.html',
                  {'user_form': user_form, 'profile_form': profile_form})

@login_required
def register_creditcard(request):
    if request.method == "POST":
        form = UserCreditcardForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse("Now you can log-in")  # this is a placeholder at present
            return HttpResponseRedirect(reverse("transactions:transaction_report"))
    elif request.method == "GET":
        form = UserCreditcardForm()
    return render(request, 'UserAdmin/Apply_creditcard.html', context={'form': form})

# @login_required
# class register_creditcard(LoginRequiredMixin, CreateView):
#     context_object_name = 'feedback'
#     form_class = UserCreditcardForm
#     template_name = 'UserAdmin/Apply_creditcard.html'
#     success_url = reverse_lazy('loading')
#
#     def get_form_kwargs(self, **kwargs):
#         form_kwargs = super(register_creditcard, self).get_form_kwargs(**kwargs)
#         form_kwargs["user"] = self.request.user
#         return form_kwargs
#
def loading(request):

        return render(request, "UserAdmin/loading.html")