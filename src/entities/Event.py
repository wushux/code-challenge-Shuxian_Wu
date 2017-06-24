class Event(object):
    """
    There are 4 types of events:
    CUSTOMER, SITE_VISIT, IMAGE, ORDER
    All the events contains key and event_time
    The customer_id in SITE_VISIT, IMAGE, ORDER is the key in CUSTOMER.
    """
    def __init__(self, key, event_time):
        self.key = key
        self.event_time = event_time

