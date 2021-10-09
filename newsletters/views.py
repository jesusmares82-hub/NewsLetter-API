from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from newsletters.models import NewsLetters
from newsletters.serializers import NewsletterSerializer
from tags.models import Tags
from tags.serializers import TagSerializer
from users.models import Users
from votes.models import Votes
from votes.serializers import VoteSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = NewsLetters.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        query = {}
        for item in self.request.query_params:
            if item in ['users', 'tags']:
                query[item + '__id'] = self.request.query_params[item]
                continue
            query[item + '__icontains'] = self.request.query_params[item]
        self.queryset = self.queryset.filter(**query)
        return super().get_queryset()

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def tags(self, request, pk=None):
        newsletter = self.get_object()
        if request.method == 'GET':
            serialized = TagSerializer(newsletter.tags, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)

        if request.method == 'POST':
            newsletter_id = request.data['tags']
            for tag_id in newsletter_id:
                tag = Tags.objects.get(id=int(tag_id))
                newsletter.tags.add(tag)
            return Response(status=status.HTTP_201_CREATED)

        if request.method == 'DELETE':
            newsletter_id = request.data['tags']
            for tag_id in newsletter_id:
                tag = Tags.objects.get(id=int(tag_id))
                newsletter.tags.remove(tag)
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['POST'], detail=True)
    def users(self, request, pk=None):
        newsletter = self.get_object()
        users_id = request.data['id']

        for user_id in users_id:
            user = Users.objects.get(id=int(user_id))
            newsletter.users.add(users_id)
        return Response(status=status.HTTP_201_CREATED)

    # Display the votes of each bulletin

    @action(methods=['GET'], detail=True)
    def votes(self, request, pk=None):
        newsletter = self.get_object()
        votes = Votes.objects.filter(newsletter=int(newsletter.id))
        serialized = VoteSerializer(votes, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
