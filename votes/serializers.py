from rest_framework import serializers

from votes.models import Votes


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Votes
        fields = '__all__'
