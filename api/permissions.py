from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    السماح بقراءة للجميع، والتعديل فقط للمشرفين (is_staff).
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    السماح للمالك (owner) أو للمشرف فقط بالتعديل.
    يُفترض أن الـ view يحتوي على object.owner أو object.author
    """
    def has_object_permission(self, request, view, obj):
        # قراءة متاحة للجميع
        if request.method in permissions.SAFE_METHODS:
            return True
        # superuser or staff
        if request.user and request.user.is_staff:
            return True
        # مالك الكائن:
        owner = getattr(obj, 'owner', None) or getattr(obj, 'author', None)
        if owner is None:
            return False
        return owner == request.user
