from rest_framework import permissions

class AllowAnyGet(permissions.BasePermission):
    """
    Custom permission to allow any GET request without authorization,
    while requiring authentication for other HTTP methods.
    """
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user and request.user.is_authenticated

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_admin
