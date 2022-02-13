from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerialaizer
from .models import User


# Create your views here.

class UserViewSet(ModelViewSet):
    serializer_class = UserSerialaizer
    queryset = User.objects.all()
