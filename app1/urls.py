from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_account, name='create_account'),
    path('success/<int:customer_ID>/', views.account_success, name='account_success'),
]
