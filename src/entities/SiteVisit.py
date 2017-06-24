from .Event import Event
class SiteVisit(Event):
    """
    Inheriting from Event
    
    {"type": "SITE_VISIT", 
    "verb": "NEW", 
    "key": "ac05e815502f", 
    "event_time": "2017-01-06T12:45:52.041Z", 
    "customer_id": "96f55c7d8f42", 
    "tags": [{"some key": "some value"}]},
    """
    def __init__(self, type, verb, key, event_time, customer_id, tags = None):
        Event.__init__(self, key, event_time)
        self.type =type
        self.verb = verb
        self.customer_id = customer_id
        self.tags = tags


