from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from votes.models import Votes
from votes.serializers import VoteSerializer


class VotesViewSet(viewsets.ModelViewSet):
    queryset = Votes.objects.all()
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticated,)
