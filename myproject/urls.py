# piggybank/urls.py
from django.urls import path
from piggybank.views import add_money, view_transactions, break_piggy_bank

urlpatterns = [
    path('add_money/', add_money, name='add_money'),
    path('view_transactions/', view_transactions, name='view_transactions'),
    path('break_piggy_bank/', break_piggy_bank, name='break_piggy_bank'),
]
