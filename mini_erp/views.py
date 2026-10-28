from django.shortcuts import render


def dashboard(request):
    return render(request, 'mini_erp/dashboard.html')

def product(request):
    return render(request, 'mini_erp/inventory/product_master.html')
