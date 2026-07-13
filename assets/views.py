from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def assets(request):
    return render(request, "assets/assets.html")


def asset_detail(request):
    return render(request, "assets/asset_detail.html")


def add_asset(request):
    return render(request, "assets/add_asset.html")


def edit_asset(request):
    return render(request, "assets/edit_asset.html")


def delete_asset(request):
    return render(request, "assets/delete_asset.html")


def asset_categories(request):
    return render(request, "assets/asset_categories.html")


def add_category(request):
    return render(request, "assets/add_category.html")


def edit_category(request):
    return render(request, "assets/edit_category.html")


def asset_assignment(request):
    return render(request, "assets/asset_assignment.html")


def assign_asset(request):
    return render(request, "assets/assign_asset.html")


def transfer_asset(request):
    return render(request, "assets/transfer_asset.html")


def return_asset(request):
    return render(request, "assets/return_asset.html")


def asset_history(request):
    return render(request, "assets/asset_history.html")


def asset_qrcode(request):
    return render(request, "assets/asset_qrcode.html")


def asset_search(request):
    return render(request, "assets/asset_search.html")


def asset_labels(request):
    return render(request, "assets/asset_labels.html")