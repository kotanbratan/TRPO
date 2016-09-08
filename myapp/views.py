from django.shortcuts import render
from django.http.response import HttpResponse#, HttpResponseRedirect, Http404
#from django.contrib.auth.models import User
#from django.http import JsonResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
#from django.contrib.auth import login, logout
#from django.contrib.auth.decorators import login_required
from myapp.models import Bid, Partner, Product, Status, Type


# Create your views here.
def MainView (request):
    #bids = Bid.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myapp/main.html', {})

def temp_one (request):
    view = "temp_one"
    html = "<html><body>This is %s view</html></body>" % view
    return HttpResponse(html)

def temp_two (request):
    view = "temp_two"
    t = get_template('temp.html')
    html = t.render(Context({'name': view}))
    return HttpResponse(html)

def temp_three (request):
    view = "temp_three"
    return render_to_response('temp.html', {'name': view})

def BidsList(request):
    return render_to_response('bids.html', {'bids': Bid.objects.all()})

def BidView(request, bid_id = 1):
    return render_to_response('bid.html', {'bid': Bid.objects.get(id=bid_id)})#, 'product': Product.objects.filter(product_bid_id=bid_id)})

def StatusEdit(request, bid_id = 1):
    return render_to_response('StatusEdit.html', {'status': Status.objects.get(id=bid_id)})

def ProductsList(request):
    return render_to_response('products.html', {'products': Product.objects.all()})

def PartnersList(request):
    return render_to_response('partners.html', {'partners': Partner.objects.all()})

def NewBidView(request, bid_id = 1):
    return render_to_response('NewBid.html', {'bid': Bid.objects.get(id=bid_id)})

def BidEditView (request, bid_id = 1, bid_partner_id = 1):
    return render_to_response('BidEdit.html', {'bid': Bid.objects.get(id=bid_id), 'products': Product.objects.all(), 'statuses': Status.objects.all(), 'partner': Partner.objects.filter(id=bid_partner_id)})
