from django.shortcuts import render


def settings(request):
    return render(request, "settings/settings.html")


def users(request):
    return render(request, "settings/users.html")


def add_user(request):
    return render(request, "settings/add_user.html")


def edit_user(request, id):
    return render(request, "settings/edit_user.html")


def roles(request):
    return render(request, "settings/roles.html")


def permissions(request):
    return render(request, "settings/permissions.html")


def system_logs(request):
    return render(request, "settings/system_logs.html")


def backup_restore(request):
    return render(request, "settings/backup_restore.html")