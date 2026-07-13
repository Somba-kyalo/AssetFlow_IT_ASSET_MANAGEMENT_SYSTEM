from django.urls import path
from . import views

urlpatterns = [

    path("", views.suppliers, name="suppliers"),

    path("supplier_detail/<int:id>/", views.supplier_detail, name="supplier_detail"),

    path("add_supplier/", views.add_supplier, name="add_supplier"),

    path("edit_supplier/<int:id>/", views.edit_supplier, name="edit_supplier"),

    path("delete_supplier/<int:id>/", views.delete_supplier, name="delete_supplier"),

    path("supplier_assets/<int:id>/", views.supplier_assets, name="supplier_assets"),

    path("supplier_history/<int:id>/", views.supplier_history, name="supplier_history"),

]