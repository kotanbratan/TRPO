#from myapp.base import BaseRecord


class BidRecord(BaseRecord):
    TABLE_NAME = 'myapp_bid'
    FIELDS = {
        'id',
        'date',
        'manager',
        'bid_partner',
        'bid_type',
        'bid_status',
        'bid_product',
        'amount'
}

class ProductRecord(BaseRecord):
    TABLE_NAME = 'myapp_product'
    FIELDS = {
        'id',
        'product_name',
        'price'
}


class PartnerRecord(BaseRecord):
    TABLE_NAME = 'myapp_partner'
    FIELDS = {
        'id',
        'partner_name',
        'partner_phone',
        'organization'
}
