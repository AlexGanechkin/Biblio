from rest_framework import permissions

from readers.models import Reader


class ReaderPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj: Reader) -> bool:
        return obj.username == request.user.username or request.user.is_staff


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
