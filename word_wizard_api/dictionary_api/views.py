from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


from .models import Users, Words, UserWords
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
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class WordViewSet(BaseModelViewSet):
    queryset = Words.objects.all()
    serializer_class = WordSerializer


class UserWordViewSet(BaseModelViewSet):
    queryset = UserWords.objects.all()
    serializer_class = UserWordSerializer

class UserWordListAPIView(APIView):
    def get(self, request, user_id, format=None):
        user_words = UserWords.objects.filter(UserID=user_id)
        serializer = UserWordSerializer(user_words, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserWordDetailAPIView(APIView):
    def get(self, request, user_id, word_id, format=None):
        user_word = get_object_or_404(UserWords, UserID=user_id, WordID=word_id)
        serializer = UserWordSerializer(user_word)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class UserWordViewSet(BaseModelViewSet):
#     queryset = UserWords.objects.filter(UserID)
#     serializer_class = UserWordSerializer
