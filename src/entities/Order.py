from .Event import Event
from .Customer import Customer
class Order(Event):
    """
    Inheriting from Event
    
    {"type": "ORDER", 
    "verb": "NEW", 
    "key": "68d84e5d1a43", 
    "event_time": "2017-01-06T12:55:55.555Z", 
    "customer_id": "96f55c7d8f42", 
    "total_amount": "12.34 USD"}]
    """
    def __init__(self, type, verb, key, event_time, customer_id, total_amount):
        Event.__init__(self, key, event_time)
        self.type = type
        self.verb = verb
        self.customer_id = customer_id
        self.total_amount = total_amount
