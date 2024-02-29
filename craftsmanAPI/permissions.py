from rest_framework.permissions import SAFE_METHODS
from rest_framework.permissions import BasePermission
from .models import Craftsman, Visitor


class IsAdminOrCraftsmanOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        try:
            user = request.user
            is_craftsman = False
            if not user.is_anonymous:
                Craftsman.objects.get(user=user)
                is_craftsman = True
        except Craftsman.DoesNotExist:
            is_craftsman = False
        return bool(is_craftsman or request.user.is_staff)
    
class OnlyCraftsman(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        try:
            user = request.user
            if not user.is_anonymous:
                Craftsman.objects.get(user=user)
                return True
            return False
        except Craftsman.DoesNotExist:
            return False

class OnlyAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user.is_authenticated and request.user.is_staff)
    
class OnlyAuthenticatedVisitor(BasePermission):
    def has_permission(self, request, view):
        print('this works')
        if request.method in SAFE_METHODS:
            return True
        try:
            user = request.user
            print('user: ', user)
            if not user.is_anonymous:
                print('this works 2')
                Visitor.objects.get(user=user)
                return True
            return False
        except Visitor.DoesNotExist:
            return False
        
class IsAdminOrAuthenticatedVisitor(BasePermission):
    def has_permission(self, request, view):
        try:
            user = request.user
            if user.is_anonymous:
                return False
            Visitor.objects.get(user=user)
            is_visitor = True
        except Visitor.DoesNotExist:
            is_visitor = False
        return bool(is_visitor or request.user.is_staff)