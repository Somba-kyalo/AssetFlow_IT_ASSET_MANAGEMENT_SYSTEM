from django.urls import path
from . import views

urlpatterns = [

    path("assets/", views.assets, name="assets"),

    path("asset/<int:id>/", views.asset_detail, name="asset_detail"),

    path("add-asset/", views.add_asset, name="add_asset"),

    path("edit-asset/<int:id>/", views.edit_asset, name="edit_asset"),

    path("delete-asset/<int:id>/", views.delete_asset, name="delete_asset"),

    path("asset-categories/", views.asset_categories, name="asset_categories"),

    path("add-category/", views.add_category, name="add_category"),

    path("edit-category/<int:id>/", views.edit_category, name="edit_category"),

    path("asset-assignment/", views.asset_assignment, name="asset_assignment"),

    path("assign-asset/", views.assign_asset, name="assign_asset"),

    path("transfer-asset/<int:id>/", views.transfer_asset, name="transfer_asset"),

    path("return-asset/<int:id>/", views.return_asset, name="return_asset"),

    path("asset-history/<int:id>/", views.asset_history, name="asset_history"),

    path("asset-qrcode/<int:id>/", views.asset_qrcode, name="asset_qrcode"),

    path("asset-search/", views.asset_search, name="asset_search"),

    path("asset-labels/", views.asset_labels, name="asset_labels"),

]