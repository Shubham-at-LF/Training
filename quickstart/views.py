"""noob file"""
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from quickstart.serializers import GroupSerializer, UserSerializers   

class UserViewSet(viewsets.ModelViewSet): 
    """Class represent"""

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """Class represent"""


    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
