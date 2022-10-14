from rest_framework import permissions

SAFE_METHODS = ("GET", "HEAD", "OPTIONS")


class IsAdmOrSafeMethod(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or request.user.is_superuser == True)
