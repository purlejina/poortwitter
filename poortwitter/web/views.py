from email import message
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models.tweet import Tweet

def index(request):
    context = {}
    response = render(request, 'web/index.html', context)
    return response

def tweets(request): 
    tweets = Tweet.objects.all()
    sort_type = request.GET['sort']
    if sort_type == 'datetime':
        sorted_tweets = tweets.order_by('-datetime')
    else:
        sorted_tweets = tweets.order_by('name')

    tweet_list = [] 
    for tweet in sorted_tweets: 
        tweet_list.append({'name': tweet.name,'message':tweet.message,'datetime':tweet.datetime.strftime('%m/%d/%Y, %H:%M:%S')}) 
        
    return JsonResponse(tweet_list, safe=False) 

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        message = request.POST.get('message', None)
        if name and message:
            tweet = Tweet(name=name, message=message)
            tweet.save()
    return JsonResponse({})