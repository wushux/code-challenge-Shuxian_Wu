from .Event import Event
from .Customer import Customer
class Image(Event):
    """
    inheriting from Event
    
    {"type": "IMAGE", 
    "verb": "UPLOAD", 
    "key": "d8ede43b1d9f", 
    "event_time": "2017-01-06T12:47:12.344Z", 
    "customer_id": "96f55c7d8f42", 
    "camera_make": "Canon", 
    "camera_model": "EOS 80D"},
    """
    def __init__(self, type, verb, key, event_time, customer_id, camera_make = None, camera_model = None):
        Event.__init__(self, key, event_time)
        self.type = type
        self.verb = verb
        self.customer_id = customer_id
        self.camera_make = camera_make
        self.camera_model = camera_model
