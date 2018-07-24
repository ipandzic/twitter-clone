from rest_framework import generics

from tweets.models import Tweet

from .pagination import StandardResultsPagination
from .serializers import TweetModelSerializer


class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        return Tweet.objects.all()
