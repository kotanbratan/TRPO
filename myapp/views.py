from django.shortcuts import render
from django.http.response import HttpResponse#, HttpResponseRedirect, Http404
from django.utils import timezone
#from django.contrib.auth.models import User
#from django.http import JsonResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.shortcuts import redirect
#from django.contrib.auth import login, logout
#from django.contrib.auth.decorators import login_required
from myapp.models import Bid, Partner, Product, Status, Type
from myapp.forms import BidForm

# Create your views here.
def MainView (request):
    return render(request, 'profile/main.html', {})

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
    return render_to_response('bid.html', {'bid': Bid.objects.get(id=bid_id)})

def StatusEdit(request, bid_id=1):
    status_form = StatusForm
    args = {}
    args['bid'] = Bid.objects.get(id=bid_id)
    args['statuses'] = Status.objects.all()
    args['form'] = status_form
    return render_to_response('StatusEdit.html', args)

def ProductsList(request):
    return render_to_response('products.html', {'products': Product.objects.all()})

def PartnersList(request):
    return render_to_response('partners.html', {'partners': Partner.objects.all()})

def NewBidView(request):
    #    form = BidForm()
    #    return render(request, 'myapp/NewBid.html', {'form': form})
        if request.method == "POST":
            form = BidForm(request.POST)
            if form.is_valid():
                bid = form.save(commit=False)
                bid.date = timezone.now()
                bid.manager = request.user
                bid.bid_partner = request.POST.get('partner')
                bid.bid_type = request.POST.get('type')
                bid.bid_status = request.POST.get('status')
                bid.bid_product = request.POST.get('product')
                bid.amount = request.POST.get('amount')
                bid.save()
                return redirect('myapp.views.BidView', pk=bid.pk)
        else:
            form = BidForm()
        return render(request, 'myapp/NewBid.html', {'form': form})


def BidEditView (request, bid_id = 1):
    return render_to_response('BidEdit.html', {'bid': Bid.objects.get(id=bid_id), 'products': Product.objects.all(), 'statuses': Status.objects.all(), 'partners': Partner.objects.all()})
