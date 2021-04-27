from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsProductUserOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
            return obj == request.user or request.user.is_superuser or request.user.is_staff
