from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Manager").exists()
    

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        # The IsAdminUser permission class will deny permission to any user, unless user.is_staff is True in which case permission will be allowed
        return request.user.is_authenticated and (not request.user.is_staff)
        # user, not belonging to any group = Customer
        # return request.user.is_authenticated and self.request.user.groups.count() == 0


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        # return (request.method in SAFE_METHODS) and request.user.is_authenticated
        return request.method in SAFE_METHODS