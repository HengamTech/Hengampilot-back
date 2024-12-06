from rest_framework import permissions

# Custom permission class to allow access to the object if the user is either an admin or the business owner
class IsOwnerOrAdmin(permissions.BasePermission):
    # Method to check if the user has permission for the specific object
    def has_object_permission(self, request, view, obj):
        # Allow access if the user is an admin
        if request.user.is_admin:
            return True
        
        # Allow access if the user is the business owner
        return obj.business_owner == request.user
