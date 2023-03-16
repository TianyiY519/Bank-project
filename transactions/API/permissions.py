from rest_framework import permissions


class IsInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        # print(request.user.profile.is_instructor)
        if request.user.is_superuser:
            # print("has-permission - request.user.is_superuser")
            return True
        elif request.method in permissions.SAFE_METHODS:
            # print("has-permission - permissions.SAFE_METHODS")
            return True
        elif hasattr(request.user, "profile"):
            if request.user.profile.is_manager: #这样就只有manager可以改
                # print("has-permission - request.user.profile.is_instructor")
                return True
        return False

    def has_object_permission(self, request, view, obj):
        # print(request.user.profile.is_instructor)
        print(request.user.first_name)
        if request.user.is_superuser:
            # print("has_object_permission - request.user.is_superuser")
            return True
        elif request.method in permissions.SAFE_METHODS:
            # print("has_object_permission - permissions.SAFE_METHODS")
            return True
        elif hasattr(request.user, "profile"):
            if obj.manager == request.user and request.user.profile.is_manager:
                # print("has_object_permission - request.user.profile.is_instructor and request.user.profile.is_instructor")
                return True
        return False
