from django.urls import path
from . import views

urlpatterns = [

    path("employees/", views.employees, name="employees"),

    path("employee/<int:id>/", views.employee_detail, name="employee_detail"),

    path("add-employee/", views.add_employee, name="add_employee"),

    path("edit-employee/<int:id>/", views.edit_employee, name="edit_employee"),

    path("delete-employee/<int:id>/", views.delete_employee, name="delete_employee"),

    path("employee-assets/<int:id>/", views.employee_assets, name="employee_assets"),

    path("employee-profile/<int:id>/", views.employee_profile, name="employee_profile"),

]