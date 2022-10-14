from rest_framework.permissions import BasePermission

from movies.permissions import SAFE_METHODS


class IsAdmOrCriticOrSafeMethod(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or (
            request.user.is_authenticated
            and (request.user.is_critic or request.user.is_superuser)
        )


class IsCriticOwner(BasePermission):
    def has_object_permission(self, request, view, review):

        return review.critic.id == request.user.id or request.user.is_superuser
