from rest_framework import serializers

from .models import Users, Words, UserWords


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True


class UserSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Users
        fields = "__all__"


class WordSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Words
        fields = "__all__"


class UserWordSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = UserWords
        fields = "__all__"
