
from rest_framework import serializers

from readers.models import Reader


class ReaderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reader
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'is_active']


class ReaderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reader
        fields = '__all__'


class ReaderCreateSerializer(serializers.ModelSerializer):
    """ При создании пользователя созадется только сам пользователь, книги добавить нельзя """
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Reader
        fields = ['id', 'first_name', 'last_name', 'phone_number']

    # def validate_author(self, author):
    #     if author.id == 2:
    #         raise serializers.ValidationError('Нет автора с таким id')


class ReaderUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reader
        fields = ['first_name', 'last_name', 'phone_number', 'is_active', 'books']

    def validate_books(self, data):
        if len(data) > 3:
            raise serializers.ValidationError('Больше трех не выдавать!')
        return data


class ReaderDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ['id']
