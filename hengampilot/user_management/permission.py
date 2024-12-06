from rest_framework import permissions


# Custom permission class to allow access only to the owner or admin
class IsOwnerOrAdmin(permissions.BasePermission):

    # Check if the user has permission to access the object
    def has_object_permission(self, request, view, obj):
        # Grant access if the object is the user themselves or if the user is an admin
        return obj == request.user or request.user.is_admin
