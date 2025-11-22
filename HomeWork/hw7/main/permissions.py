# main/permissions.py
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Дозволяє редагування лише адміністраторам,
    інші користувачі лише читають.
    """
    def has_permission(self, request, view):        
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
