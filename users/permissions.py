from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST' and not request.user.is_authenticated:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if view.action == 'destroy' and request.user != obj.user:
            return False

        return True
