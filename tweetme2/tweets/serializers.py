
from rest_framework import serializers
from .models import Tweet, TweetLike

MAX_LENGTH = 240
class TweetSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField('get_likes')
    retweets_count = serializers.SerializerMethodField('get_retweets')
    def get_likes(self,obj):
        return obj.likes.all().count()
    def get_retweets(self,obj):
        return obj.retweets.all().count()

    class Meta:
        model = Tweet
        fields = ['id','user','content', 'pub','hour','likes_count','retweets_count']

    def validate_content(self, text):
        if len(text)> MAX_LENGTH:
            raise serializers.ValidationError("Too long tweet")
        return text
class TweetLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetLike
        fields = ['id','user','tweet']