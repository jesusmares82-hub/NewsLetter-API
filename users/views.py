from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from newsletters.models import NewsLetters
from newsletters.serializers import NewsletterSerializer
from users.models import Users
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    # Seek
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
    def newsletters(self, request, pk=None):
        user = self.get_object()

        # As a user i want to log in so I can see the newsletters I am subscribed to.
        if request.method == 'GET':
            id = NewsLetters.objects.filter(users=int(user.id))
            serialized = NewsletterSerializer(id, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)

        # As a user i want to be able to subscribe to a newsletter to receive related news in my mailbox.
        if request.method == 'POST':
            id_user = user.id
            newsletters_id = request.data['id']
            for newsletter_id in newsletters_id:
                newsletter = NewsLetters.objects.get(id=int(newsletter_id))
                newsletter.users.add(id_user)
            return Response(status=status.HTTP_201_CREATED)

        # As a user i want to be able to unsubscribe from the newsletters to stop receiving news.
        if request.method == 'DELETE':
            id_user = user.id
            newsletters_id = request.data['id']
            for newsletter_id in newsletters_id:
                newsletter = NewsLetters.objects.get(id=int(newsletter_id))
                newsletter.users.remove(id_user)
            return Response(status=status.HTTP_204_NO_CONTENT)
