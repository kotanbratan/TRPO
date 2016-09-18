from django.utils import timezone

#from myapp.records import BidRecord, ProductRecord, PartnerRecord

class BidDomain:
    bid = None

    @staticmethod
    def get_all_bids():
        return Bid.objects.all()

    @classmethod
    def create_bid(self, bid_data=None):
        errors = self.validate(bid_data)
        if self.bid is None and not errors:
            bid = BidRecord(date=timezone.now,
                            manager=bid_data['manager'],
                            bid_partner=bid_data['bid_partner'],
                            bid_type=bid_data['bid_type'],
                            bid_status=bid_data['bid_status'],
                            bid_product=bid_data['bid_product'],
                            amount=bid_data['amount'])

            bid.save()
        else:
            return errors

    @classmethod
    def validate(self, bid_data):
        errors = {}

        if not "manager" in bid_data:
           errors['manager'] = {
               "message": "Обязательноe поле"
           }

        if not "bid_partner" in bid_data:
            errors['bid_data'] = {
                "message": "Обязательноe поле"
            }

        return errors

    @classmethod
    def change_bid(self, bid_data):
        errors = self.validate(bid_data)
        if self.bid is None and not errors:
            self.bid = BidRecord(date=timezone.now,
                            manager=bid_data['manager'],
                            bid_partner=bid_data['bid_partner'],
                            bid_type=bid_data['bid_type'],
                            bid_status=bid_data['bid_status'],
                            bid_product=bid_data['bid_product'],
                            amount=bid_data['amount'])

            self.bid.save()
        else:
            return errors

    @classmethod
    def change_status(self, bid):
            errors = self.validate(bid_data)
            if self.bid is None and not errors:
                self.bid = BidRecord(bid_status=bid_data['bid_status'],)

                self.bid.save()
            else:
                return errors

    @classmethod
    def remove_bid(self):
        return self.bid.delete()


class ProductDomain:
    product = None

    @staticmethod
    def get_all_products():
        return Product.objects.all()


class PartnerDomain:
    partner = None

    @staticmethod
    def get_all_partners():
        return Partner.objects.all()

class StatusDomain:
    partner = None

class TypeDomain:
    partner = None
