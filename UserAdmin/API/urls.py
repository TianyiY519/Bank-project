from django.urls import path
# from .views import json_course_list, json_get_specific_course
from .views import api_user_list, api_user_detail, ContactUsList, ContactUsDetail, api_creditcard_list, logout_view, api_creditcard_detail
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('courses/', json_course_list, name='api_json_all_courses'),
    # path('courses/json_get_specific_course/<int:course_id>/', json_get_specific_course, name='api_json_get_specific_course'),

    path('vfs_list/', api_user_list, name='transaction_vfs_list'),  # New Entry
    path('vfs_detail/<int:pk>', api_user_detail, name='transaction_vfs_detail'), # New Entry
    path('queries/', ContactUsList.as_view(), name='courses_queries_list'),
    path('query_detail/<int:pk>', ContactUsDetail.as_view(), name='courses_query_detail'),
    path('creditcard_detail/<int:pk>', api_creditcard_detail, name='creditcard_detail'),  # New Entry
    path('', api_creditcard_list, name='creditcard_list'),
    path('login/', obtain_auth_token, name='user_admin_login'),
    path('logout/', logout_view, name='user_admin_logout'),
    # path('register_user/', user_registration_view, name='user_admin_register_user'),
]