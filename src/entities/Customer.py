from .Event import Event
class Customer( Event):
    """
    Inheriting from Event
    
    Sample data in json:
    {"type": "CUSTOMER", 
    "verb": "NEW", 
    "key": "96f55c7d8f42", 
    "event_time": "2017-01-06T12:46:46.384Z", 
    "last_name": "Smith", 
    "adr_city": "Middletown", 
    "adr_state": "AK"},
    """

    def __init__(self, type, verb, key, event_time, last_name = None, adr_city = None, adr_state = None):
        Event.__init__(self, key, event_time)
        self.type = type
        self.verb = verb
        self.last_name = last_name
        self.adr_city = adr_city
        self.adr_state = adr_state


    
