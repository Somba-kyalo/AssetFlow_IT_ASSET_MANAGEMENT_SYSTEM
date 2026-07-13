from django.urls import path
from . import views

urlpatterns = [

    path("departments/", views.departments, name="departments"),

    path("department/<int:id>/", views.department_detail, name="department_detail"),

    path("add-department/", views.add_department, name="add_department"),

    path("edit-department/<int:id>/", views.edit_department, name="edit_department"),

    path("delete-department/<int:id>/", views.delete_department, name="delete_department"),

    path("department-assets/<int:id>/", views.department_assets, name="department_assets"),

]