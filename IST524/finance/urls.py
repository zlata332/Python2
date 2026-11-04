from django.urls import path
from finance.views import (
    created_finance_view,
    read_finance_view,
    delete_finance_view,
    update_finance_view
)

urlpatterns = [
    path('create_finance/', created_finance_view, name='create'),
    path('finance_list/', read_finance_view, name='finance_list'),
    path('finance_list/<int:id>/update/', update_finance_view, name='update'),
    path('finance_list/<int:id>/delete/', delete_finance_view, name='delete'),
]