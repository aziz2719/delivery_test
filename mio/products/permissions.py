from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsProductUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_superuser or request.user.is_staff


class IsCommentsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'DELETE':
            return obj.user == request.user or request.user.is_staff or request.user.is_superuser