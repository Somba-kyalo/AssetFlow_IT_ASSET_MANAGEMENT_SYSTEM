from django.urls import path
from . import views

urlpatterns = [

    path("settings/", views.settings, name="settings"),

    path("settings/users/", views.users, name="users"),

    path("settings/users/add/", views.add_user, name="add_user"),

    path("settings/users/<int:id>/edit/", views.edit_user, name="edit_user"),

    path("settings/roles/", views.roles, name="roles"),

    path("settings/permissions/", views.permissions, name="permissions"),

    path("settings/system_logs/", views.system_logs, name="system_logs"),

    path("settings/backup_restore/", views.backup_restore, name="backup_restore"),

]