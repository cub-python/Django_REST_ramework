from rest_framework import serializers
from test_models import User, Brend, Biography


class UserSerializer(serializers.Serializer):
   name = serializers.CharField(max_length=128)
   birthday_year = serializers.IntegerField()


class BiographySerializer(serializers.Serializer):
   text = serializers.CharField(max_length=1024)
   user = UserSerializer()


class BrendSerializer(serializers.Serializer):
   name = serializers.CharField(max_length=128)
   user = UserSerializer(many=True)


user1 = User('Henry', 1863)
serializer = UserSerializer(user1)
print(serializer.data)

biography = Biography('Текст биографии', user1)
serializer = BiographySerializer(biography)
print(serializer.data)

user2 = User('Karl', 1864)
brend = Brend('World cars', [user1, user2])

serializer = BrendSerializer(brend)
print(serializer.data)