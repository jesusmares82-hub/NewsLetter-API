from rest_framework import serializers

from newsletters.models import NewsLetters


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetters
        fields = '__all__'
