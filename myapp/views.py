from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
#from django.contrib.auth.models import User
from django.http import JsonResponse
#from django.contrib.auth import login, logout
#from django.contrib.auth.decorators import login_required
from .models import Bid


# Create your views here.
def MainView (request):
    #bids = Bid.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myapp/main.html', {})
