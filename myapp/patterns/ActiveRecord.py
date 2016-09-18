from myapp.models import Bid

class Bid():
    nomer=0
    date=''
    manager=''
    bid_partner=''
    bid_type=''
    bid_status=''
    amount=0

    def create(self, date, manager, bid_partner, bid_type, bid_status, amount):
        p=Bid.objects.create(date=date, manager=manager, bid_partner=bid_partner, bid_type=bid_type, bid_status=bid_status, amount=amount)

    def read(self, pk):
        p=Bid.objects.get(id=pk)
        return p

    def update_status(self, pk, bid_status):
        p=Bid.objects.get(id=pk).update(bid_status=bid_status)

    def delete(self, pk):
        p=Bid.objects(id=pk).delete()

    def update(self, pk):
        p=Bid.objects.get(id=pk).update(bid_status=bid_status)
        p=Bid.objects.get(id=pk).update(bid_product=bid_product)
        p=Bid.objects.get(id=pk).update(amount=amount)

    def get_all(self):
        return Bid.objects.all()
