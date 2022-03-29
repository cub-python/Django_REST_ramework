import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from users_app.models import User, Brend


# level 1
# class Query(ObjectType):
#     hello = graphene.String(default_value="Hi")
#
#
# schema = graphene.Schema(query=Query)

# level 2
# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = '__al__'
#

# class Query(ObjectType):
#     users = graphene.List(UserType)
#
#     def resolve_users(root, info):
#         return User.objects.all()
#
#
# schema = graphene.Schema(query=Query)

# level 3
# class BrendType(DjangoObjectType):
#     class Meta:
#         model = Brend
#         fields = '__all__'
#
# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email')
#
#
# class Query(ObjectType):
#     users = graphene.List(UserType)
#     brends = graphene.List(UserType)
#
#     def resolve_users(root, info):
#         return User.objects.all()
#
#     def resolve_brends(root, info):
#         return Brend.objects.all()

# schema = graphene.Schema(query=Query)

#  level 4
# class BrendType(DjangoObjectType):
#     class Meta:
#         model = Brend
#         fields = '__all__'
#
# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')
#
#
# class Query(ObjectType):
#
#    user_id = graphene.Field(UserType,id=graphene.Int(required=True))
#    def resolve_user_id(root,info,id=None):
#        try:
#            return User.objects.get(id=id)
#        except User.DoesNotExist:
#            return None
#    brends_by_user = graphene.List(BrendType, first_name=graphene.String(required=False))
#    def resolve_brends_by_user(root,info,first_name=None):
#        brends = Brend.objects.all()
#        if first_name:
#            brends = brends.filter(users__first_name=first_name)
#
#        return brends
#
#
# schema = graphene.Schema(query=Query)


#  level 5 (метод мутация (создание,удаление,обновление))

class BrendType(DjangoObjectType):
    class Meta:
        model = Brend
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class Query(ObjectType):
    user_id = graphene.Field(UserType, id=graphene.Int(required=True))

    def resolve_user_id(root, info, id=None):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    brends_by_user = graphene.List(BrendType, first_name=graphene.String(required=False))

    def resolve_brends_by_user(root, info, first_name=None):
        brends = Brend.objects.all()
        if first_name:
            brends = brends.filter(users__first_name=first_name)

        return brends
#
#
# class UserUpdateMutation(graphene.Mutation):
#     class Arguments:
#         birthday_year = graphene.Int(required=True)
#         id = graphene.ID()
#
#     user = graphene.Field(UserType)
#
#     @classmethod
#     def mutate(cls, root, info, birthday_year, id):
#         user = User.objects.get(id=id)
#         user.birthday_year = birthday_year
#         user.save()
#         return UserUpdateMutation(user=user)
#
#
# class Mutations(ObjectType):
#     update_user = UserUpdateMutation.Field()

# class UserCreateMutation(graphene.Mutation):
#
#     class Arguments:
#         first_name = graphene.String()
#         last_name = graphene.String()
#         birthday_year = graphene.Int(required=True)
#         # id = graphene.ID()
#
#     user = graphene.Field(UserType)
#
#     @classmethod
#     def mutate(cls, root, info,first_name, last_name,birthday_year,):
#         user = User(first_name=first_name,last_name=last_name,birthday_year=birthday_year)
#         user.save()
#         return UserCreateMutation(user=user)
#
#
# class Mutations(ObjectType):
#     update_user = UserUpdateMutation.Field()
#     create_user = UserCreateMutation.Field()
# schema = graphene.Schema(query=Query,mutation=Mutations)

schema = graphene.Schema(query=Query)
