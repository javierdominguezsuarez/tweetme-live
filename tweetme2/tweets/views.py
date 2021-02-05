
from django.http.response import JsonResponse
from django.shortcuts import  render
from rest_framework import permissions
from rest_framework.decorators import action, api_view, permission_classes  
from rest_framework.response import Response
from .models import Tweet, TweetLike
from .forms import TweetForm
from rest_framework.permissions import IsAuthenticated
from .serializers import TweetSerializer
from rest_framework import viewsets
from account.models import Profile
########################################################################

#Using old django
def home_view(request, *args, **kwargs):
    return render (request,"pages/home.html", context = {}, status = 200)

def tweet_detail_view_old(request, tweet_id, *args , **kwargs):
    """
    REST API VIEW 
    Consume by JavaScript  
    return json data 
    """
    data = {
        "id": tweet_id,
        #image also
    }
    status = 200
    try:
        obj = Tweet.objects.get(id = tweet_id)
        data["content"] = obj.content
    except: 
        data["content"] = "Not found"
        status = 404
    return JsonResponse(data, status = status)

def tweet_list_view_old (request, *args, **kwargs):
    """
    REST API VIEW 
    Consume by JavaScript  
    return json data 
    """
    tweet_list = Tweet.objects.all()
    data_list = [{"id": t.id,"content": t.content, "likes": 0} for t in tweet_list]
    data = {
        "isUser": False ,
        "response": data_list
    }
    return JsonResponse(data_list,safe= False)

def tweet_create_view_old (request, *args, **kwargs):
    """
    REST API CREATE VIEW 
    """
    form = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit = False)
        obj.save()
        form = TweetForm()
    return render(request, 'components/forms.html', context = {"form" : form})
#################################################################################

# Using django rest framework

@api_view(['GET'])
def tweet_detail_view (request,tweet_id,  *args, **kwargs):
    obj = Tweet.objects.get(id = tweet_id)
    if not obj.exists():
        return Response({}, status = 404)
    serializer = TweetSerializer(obj)
    return Response(serializer.data, status = 200)

@api_view(['GET'])
def tweet_list_view (request, *args, **kwargs):
    tweet_list = Tweet.objects.all()
    serializer = TweetSerializer(tweet_list, many = True)
    return Response(serializer.data, status = 200)



@api_view(['POST'])
#comprueba que el usuario tenga credenciales
@permission_classes([IsAuthenticated])
def tweet_create_view (request,*args,**kwargs):
    """
    REST API CREATE VIEW 
    """
    serializer = TweetSerializer(data = request.data )
    #raise_exception devuelve un json con el error si lo hubiera
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status = 201)  

    #return Response({"Error" : "Invalid content"}, status = 400)

   
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def tweet_delete_view (request,tweet_id,  *args, **kwargs):
    obj = Tweet.objects.get(id = tweet_id)
    if not obj.exists():
        return Response({}, status = 404)
    us = obj.filter(user = request.user)
    if not us.exists():
        return Response({"message": "You cannot delete "}, status = 401)
    
    obj.delete()
    
    return Response({"message":  "Tweet removed"}, status = 200)

 #########################################################################
    
#viewSetsImplementation

authenticatedActions = ['create','update','partial_update','destroy']
class TweetViewSet(viewsets.ModelViewSet):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()

    def get_permissions(self):
        if self.action in authenticatedActions:
            self.permission_classes =[permissions.IsAuthenticated]
        else :
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()

    def get_queryset(self):
        try:
            profile =  Profile.objects.filter(user = self.request.user.id)
            pro = profile.first()
            following = pro.followers.all()
            users = [i.user.id  for i in  following]
            return Tweet.objects.filter( user__in = users)
        except: 
            return Tweet.objects.all()

    @action (detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def retweet (self,request, tId):
        try :
            userRetweet = self.request.user
            tweet = Tweet.objects.filter(id = tId)
            Tweet.objects.create(user = self.request.user, content = tweet.first().content)
        except :
            return Response({"error":"no se ha podido hacer el retweet"},404)
    
    @action (detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like (self,request, tId):
        try :
            
            profile =  Profile.objects.filter(user = self.request.user.id)
            pro = profile.first()
            tweetDos = Tweet.objects.filter(id = tId).first()
            TweetLike.objects.create(profile = pro, tweet = tweetDos )
        except :
            return Response({"error":"no se ha podido hacer like"},404)
        