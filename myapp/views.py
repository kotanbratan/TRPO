from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect

# Create your views here.
def bids_list(request):
    return render(request, 'myapp/bids_list.html', {})
