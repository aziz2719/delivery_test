from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_superuser or request.user.is_staff