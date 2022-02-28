import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from test_models import User


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    birthday_year = serializers.IntegerField()

    def create(self, validated_data):
        return User(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birthday_year = validated_data.get('birthday_year', instance.birthday_year)
        return instance

    # def validate_birthday_year(self, value):
    #     if value < 5:
    #         raise serializers.ValidationError('Год рождения не может быть отрицательным')
    #     return value

    def validate(self, attrs):
        if attrs['name'] == 'Gottleb' and attrs['birthday_year'] != 1834:
            raise serializers.ValidationError('Неверный год рождения Gottleba')
        return attrs


def start():
    user = User('Gottleb', 1834)
    serializer = UserSerializer(user)

    renderer = JSONRenderer()
    json_bytes = renderer.render(serializer.data)

    stream = io.BytesIO(json_bytes)
    data = JSONParser().parse(stream)

    serializer = UserSerializer(data=data)
    serializer.is_valid()
    # Продолжение скрипта №1

    # Создание
    user = serializer.save()
    print(type(user))
    print(user)

    # Обновление всех данных
    data = {'name': 'Karl', 'birthday_year': 1864}
    serializer = UserSerializer(user, data=data)
    serializer.is_valid()
    user = serializer.save()
    print(user)

    #Обновление частичное
    data = {'birthday_year': 10}
    serializer = UserSerializer(user, data=data, partial=True)
    serializer.is_valid()
    user = serializer.save()
    print(f'{user} {user.birthday_year}')


    # Проверка 1го поля
    data = {'birthday_year': 1}
    serializer = UserSerializer(user, data=data, partial=True)
    if  serializer.is_valid():
        author = serializer.save()
        print(f'{user} {user.birthday_year}')
    else:
        print(serializer.errors)

    # Проверка всех полей
    data = {'name': 'Gottleb', 'birthday_year': 2000}
    serializer = UserSerializer(user, data=data)
    if serializer.is_valid():
        user = serializer.save()
        print(user)
    else:
        print(serializer.errors)


start()