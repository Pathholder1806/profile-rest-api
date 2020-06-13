from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""

        if request.method in permissions.SAFE_METHODS:  # This return true if the user is only trying to view all the user profiles and will skip this if the user has made a request to update the profile.
            return True

        return obj.id == request.user.id
