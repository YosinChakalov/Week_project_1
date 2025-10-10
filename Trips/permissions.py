from rest_framework.permissions import BasePermission
from .models import Trip

class TripPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == "admin":
            return True 

        if request.user.role == "taxi":
            if request.method in ["POST", "PUT", "PATCH", "DELETE", "GET"]:

                return True 
            return False

        if request.user.role == "user":
            if request.method == "GET":
                return True
            return False 
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.role == "admin":
            return True
        if request.user.role == "taxi":
            if request.method in ["PUT", "PATCH", "DELETE"]:
                return obj.driver_id == request.user
            return True 
        if request.user.role == "user":
            return request.method == "GET"
        return False