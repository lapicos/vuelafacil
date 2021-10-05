
from rest_framework.permissions import BasePermission

class AccesoInfoPersonal(BasePermission):
        def has_object_permission(self, request, view, obj):
            if request.user.is_staff:
                return True
            print(obj)
            if hasattr(obj, 'username'):
                if request.user.username == obj.username:
                    return True
            else:

                if request.user.username == obj.usuario.username:
                    return True
            return False 