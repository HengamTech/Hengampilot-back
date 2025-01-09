from rest_framework.permissions import BasePermission, SAFE_METHODS

class AllowAnyGet(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_admin

class IsStaffOrAdminUser(BasePermission):
    """
    Custom permission to allow access to users who are either staff or admin.
    """
    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or request.user.is_admin)
