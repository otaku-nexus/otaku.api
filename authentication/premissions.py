from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS', 'POST']:
            return True  # Allow read and create actions without restrictions.
        return obj.author == request.user  # Adjust 'author' field as per your model.
