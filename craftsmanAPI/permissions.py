from rest_framework.permissions import SAFE_METHODS
from rest_framework.permissions import BasePermission


class IsAdminAndCraftsmanOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user or request.user.is_staff)
    
class OnlyCraftsman(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user.is_authenticated and not request.user.is_staff)