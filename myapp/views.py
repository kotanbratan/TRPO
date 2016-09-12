from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone
from django.core.urlresolvers import reverse
#from django.contrib.auth.models import User
#from django.http import JsonResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.shortcuts import redirect, get_object_or_404
#from django.contrib.auth import login, logout
#from django.contrib.auth.decorators import login_required
from myapp.models import Bid, Partner, Product, Status, Type
from myapp.forms import BidForm, BidEditForm, StatusForm

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

def BidView(request, pk = 1):
    return render_to_response('bid.html', {'bid': Bid.objects.get(id=pk)})

def StatusEdit(request, pk=1):
    bid = get_object_or_404(Bid, pk=pk)
    if request.method == "POST":
        form = StatusForm(request.POST, instance=bid)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.bid_status = Status.objects.get(pk=int(request.POST.get('bid_status')))
            bid.save()
            return redirect(reverse('bid', args=[bid.pk] ))
    else:
        form = StatusForm(instance=bid)
    return render(request, 'myapp/StatusEdit.html', {'form': form})

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
                bid.bid_partner = Partner.objects.get(pk=int(request.POST.get('bid_partner')))
                bid.bid_type = Type.objects.get(pk=int(request.POST.get('bid_type')))
                bid.bid_status = Status.objects.get(pk=int(request.POST.get('bid_status')))
                bid.bid_product = Product.objects.get(pk=int(request.POST.get('bid_product')))
                bid.amount = request.POST.get('amount')
                bid.save()
                url = "bid/{0}/".format(str(bid.pk))
                return redirect(reverse('bid', args=[bid.pk] ))
        else:
            form = BidForm()
        return render(request, 'myapp/NewBid.html', {'form': form})


def BidEditView (request, pk):
        bid = get_object_or_404(Bid, pk=pk)
        if request.method == "POST":
            form = BidEditForm(request.POST, instance=bid)
            if form.is_valid():
                bid = form.save(commit=False)
                bid.bid_status = Status.objects.get(pk=int(request.POST.get('bid_status')))
                bid.bid_product = Product.objects.get(pk=int(request.POST.get('bid_product')))
                bid.amount = request.POST.get('amount')
                bid.save()
                return redirect(reverse('bid', args=[bid.pk] ))
        else:
            form = BidEditForm(instance=bid)
        return render(request, 'myapp/BidEdit.html', {'form': form})

def DeleteView (request, pk):
    d = Bid.objects.get(id=pk)
    d.delete()
    return render_to_response('bids.html', {'bids': Bid.objects.all()})
