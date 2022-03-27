from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Project
from .models import ToDo
from users_app.models import User, Brend, Biography


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('first_name',)
        # exclude = ('first_name',)


class BiographySerializer(ModelSerializer):

    class Meta:
        model = Biography
        fields = '__all__'


class BrendSerializer(ModelSerializer):

    class Meta:
        model = Brend
        fields = '__all__'


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(ModelSerializer):

    class Meta:
        model = ToDo
        exclude = ('is_active',)
