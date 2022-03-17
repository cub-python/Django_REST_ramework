from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import User, Brend, Biography


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class BiographySerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Biography
        fields = '__all__'


class BrendSerializer(ModelSerializer):

    class Meta:
        model = Brend
        fields = '__all__'
