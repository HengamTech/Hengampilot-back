from rest_framework.permissions import BasePermission, SAFE_METHODS

    # Custom permission to allow any GET request without authorization,
    # while requiring authentication for other HTTP methods.
class AllowAnyGet(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS: # SAFE_METHODS are read-only methods
            return True
        return request.user and request.user.is_authenticated
    
    # Custom permission to allow access only to the owner or admin
class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_admin
