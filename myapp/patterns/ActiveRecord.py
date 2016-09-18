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



from django.utils import timezone

from core.model.test.records import TestRecord


class TestTransactionScript:
    test = None

    @classmethod
    def create_test(self, test_data=None):
        errors = {}

        if not "title" in test_data:
            errors['title'] = {
                "message": "Обязательноe поле"
            }

        if not "description" in test_data:
            errors['description'] = {
                "message": "Обязательноe поле"
            }

        if self.test is None and not errors:
            test = TestRecord(user_id=test_data['user'],
                              title=test_data['title'],
                              creation_date=timezone.now,
                              description=test_data['description'],
                              total_points=100)

            test.save()
        else:
            return errors

    @classmethod
    def change_test(self, test_data):
        errors = {}

        if not "title" in test_data:
            errors['title'] = {
                "message": "Обязательноe поле"
            }

        if not "description" in test_data:
            errors['description'] = {
                "message": "Обязательноe поле"
            }

        if self.test is None and not errors:
            self.test = TestRecord(user_id=test_data['user'],
                                   title=test_data['title'],
                                   creation_date=timezone.now,
                                   description=test_data['description'],
                                   total_points=100)

            self.test.save()
        else:
return errors
