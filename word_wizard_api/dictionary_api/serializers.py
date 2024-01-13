from rest_framework import serializers

from .models import User, Word, UserWord


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True


class UserSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = User
        fields = "__all__"


class WordSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Word
        fields = "__all__"


class UserWordSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = UserWord
        fields = "__all__"
