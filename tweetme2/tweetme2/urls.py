"""tweetme2 URL Configuration
"""
from django.conf.urls import include
from tweets.views import TweetViewSet
from tweets.views import home_view
#from tweets.views import tweet_detail_view, tweet_list_view, tweet_create_view,tweet_delete_view
from django.contrib import admin
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tweets', TweetViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path("apiv2/", include("account.urls")),
    path('apiv2/', include(router.urls)),
]
