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

class OnlyAdminOrCraftsman(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_anonymous:
            return False
        if user.is_staff:
            return True
        if 'craftsman_pk' in view.kwargs or 'pk' in view.kwargs:
            try:
                pk = None
                if 'craftsman_pk' in view.kwargs:
                    pk = int(view.kwargs['craftsman_pk'])
                else:
                    pk = int(view.kwargs['pk'])
                craftsman1 = Craftsman.objects.get(user=user)
                craftsman2 = Craftsman.objects.get(pk=pk)
                if craftsman1 == craftsman2:
                    return True
                else:
                    return False
            except Craftsman.DoesNotExist:
                return False
            
            
class OnlyCraftsman(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if user.is_anonymous:
            return False
        if 'craftsman_pk' in view.kwargs or 'pk' in view.kwargs:
            try:
                pk = None
                if 'craftsman_pk' in view.kwargs:
                    pk = int(view.kwargs['craftsman_pk'])
                else:
                    pk = int(view.kwargs['pk'])
                craftsman1 = Craftsman.objects.get(user=user)
                craftsman2 = Craftsman.objects.get(pk=pk)
                if craftsman1 == craftsman2:
                    return True
                else: 
                    return False
            except Craftsman.DoesNotExist:
                return False

class OnlyAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user.is_authenticated and request.user.is_staff)


class OnlyAuthenticatedVisitorCanWriteReview(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_anonymous:
            return False
        try:
           Visitor.objects.get(user=user)
           return True 
        except Visitor.DoesNotExist:
            return False
        
        
    
class OnlyAuthenticatedVisitor(BasePermission):
    def has_permission(self, request, view):
        try:
            if 'pk' in view.kwargs:
                # Visitor obtained from authenticated user
                visitor1 = Visitor.objects.get(user=request.user)
                # Visitor obtained from pk in url
                visitor2 = Visitor.objects.get(pk=int(view.kwargs['pk']))
                if visitor1 == visitor2:
                    return True
                else:
                    return False
        except Visitor.DoesNotExist:
            return False
        
# class IsAdminOrAuthenticatedVisitor(BasePermission):
#     def has_permission(self, request, view):
#         try:
#             user = request.user
#             if user.is_anonymous:
#                 return False
#             Visitor.objects.get(user=user)
#             is_visitor = True
#         except Visitor.DoesNotExist:
#             is_visitor = False
#         return bool(is_visitor or request.user.is_staff)
    
class IsAdminOrAuthenticatedVisitor(BasePermission):
    def has_permission(self, request, view):
            user = request.user
            if user.is_anonymous:
                return False
            if user.is_staff:
                return True
            if 'pk' in view.kwargs:
                try:
                    # Visitor obtained from authenticated user
                    visitor1 = Visitor.objects.get(user=user)
                    # Visitor obtained from pk in url
                    visitor2 = Visitor.objects.get(pk=int(view.kwargs['pk']))
                    if visitor1 == visitor2:
                        return True
                    else:
                        return False
                except Visitor.DoesNotExist:
                    return False