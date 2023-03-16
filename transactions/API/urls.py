from django.urls import path
# from .views import json_course_list, json_get_specific_course
from .views import api_transaction_list, api_transaction_detail, TransactionList, NewPostReview
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('courses/', json_course_list, name='api_json_all_courses'),
    # path('courses/json_get_specific_course/<int:course_id>/', json_get_specific_course, name='api_json_get_specific_course'),

    path('vfs_list/', api_transaction_list, name='transaction_vfs_list'),  # New Entry
    path('vfs_detail/<int:pk>', api_transaction_detail, name='transaction_vfs_detail'), # New Entry
    path('queries/', TransactionList.as_view(), name='courses_queries_list'),
    # path('post/<int:pk>/new_review', NewPostReview.as_view(), name='blogs_post_new_review'),
]