from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer

# Create your views here.

def create_account(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('account_success', customer_ID=customer.customer_ID)
    else:
        form = CustomerForm()
    return render(request, 'app1/create_account.html', {'form': form})

def account_success(request, customer_ID):
    return render(request, 'app1/account_success.html', {'Customer_ID': customer_ID})
