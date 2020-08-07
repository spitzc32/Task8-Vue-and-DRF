from rest_framework import permissions

"""
Task 4: Permissions
Checks if the User is Admin or if not, reading is their only option.
Solution Derived from excercises
"""

class IsAdminUserOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)

        return request.method in permissions.SAFE_METHODS or is_admin