from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return request.user.is_authenticated or request.user.is_staff
        elif view.action in ['create', 'update', 'partial_update', 'destroy']:
            return bool(request.user and request.user.is_staff)
        else:
            return False

    # def has_object_permission(self, request, view, obj):
    #
    #     if not request.user.is_authenticated:
    #         return False
    #
    #     if view.action == 'retrieve':
    #         return obj == request.user or request.user.is_admin
    #     elif view.action in ['update', 'partial_update']:
    #         return obj == request.user or request.user.is_admin
    #     elif view.action == 'destroy':
    #         return request.user.is_admin
    #     else:
    #         return False
