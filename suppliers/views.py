from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def suppliers(request):
    return render(request, "suppliers/suppliers.html")


def supplier_detail(request, id):
    return render(request, "suppliers/supplier_detail.html")


def add_supplier(request):
    return render(request, "suppliers/add_supplier.html")


def edit_supplier(request, id):
    return render(request, "suppliers/edit_supplier.html")


def delete_supplier(request, id):
    return render(request, "suppliers/delete_supplier.html")


def supplier_assets(request, id):
    return render(request, "suppliers/supplier_assets.html")


def supplier_history(request, id):
    return render(request, "suppliers/supplier_history.html")