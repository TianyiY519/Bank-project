from django.urls import path

from .views import DepositMoneyView, WithdrawMoneyView, TransactionRepostView
from . import views

app_name = 'transactions'


urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("report/", TransactionRepostView.as_view(), name="transaction_report"),
    path('page_view/', views.PostListsView.as_view(), name='blogs_list_posts_page_view'),
    path("withdraw/", WithdrawMoneyView.as_view(), name="withdraw_money"),
]
