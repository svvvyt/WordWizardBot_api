from rest_framework import mixins, viewsets

from .models import User, Word, UserWord
from .serializers import UserSerializer, WordSerializer, UserWordSerializer


class BaseModelViewSet(mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        model_class = self.queryset.model

        if not pk:
            return model_class.objects.all()

        return model_class.objects.filter(pk=pk)


class UserViewSet(BaseModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WordViewSet(BaseModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class UserWordViewSet(BaseModelViewSet):
    queryset = UserWord.objects.all()
    serializer_class = UserWordSerializer
