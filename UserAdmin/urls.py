from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register_new_user, name='useradmin_register'),
    path('login/', auth_views.LoginView.as_view(template_name='UserAdmin/login.html'), name='userdamin_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='userdamin_logout'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='UserAdmin/change_password.html'),
         name='userdamin_change_password'),
    #path('custom_login/', views.CustomLoginView.as_view(), name='userdamin_custom_login'),
    path('update_profile/', views.update_user_profile, name='userdamin_update_profile'),
    path('apply_creditcard/', views.register_creditcard, name='userdamin_apply_creditcard'),
    path('loading/', views.loading, name='loading'),
    # path('update_profile_3/', views.update_user_profile_3, name='userdamin_update_profile_3'),

]

