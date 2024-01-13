from django.urls import path, include
from rest_framework import routers

from dictionary_api.views import UserViewSet, WordViewSet, UserWordViewSet


class BaseRouter(routers.SimpleRouter):
    routes = [
        routers.Route(
            url=r'^{prefix}/$',
            mapping={'get': 'list', 'post': 'create'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        routers.Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve', 'put': 'update', 'delete': 'destroy'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
    ]


user_router = BaseRouter()
user_router.register(r'users', UserViewSet, basename='users')

word_router = BaseRouter()
word_router.register(r'words', WordViewSet, basename='words')

user_words_router = BaseRouter()
user_words_router.register(r'user-words', UserWordViewSet, basename='user-words')

urlpatterns = [
    path('api/', include(user_router.urls)),
    path('api/', include(word_router.urls)),
    path('api/users/<int:user_id>/', include(user_words_router.urls)),
    path('api/users/<int:user_id>/___/<int:word_id>', include(user_words_router.urls))

    # path('api/users/', include(user_router.urls)),
    # path('api/users/<int:user_id>/', include(user_router.urls)),
    # path('api/words/', include(word_router.urls)),
    # path('api/words/<int:word_id>/', include(word_router.urls)),  # 'words/<str:word_text>/' 'words/<int:word_id>/'
    # path('api/users/<int:user_id>/words/', include(user_words_router.urls)),
]
