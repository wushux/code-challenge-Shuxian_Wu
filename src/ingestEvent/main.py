from src.entities.Event import Event
from src.entities.Customer import Customer
from src.entities.SiteVisit import SiteVisit
from src.entities.Image import Image
from src.entities.Order import Order
from src.entities.Data import Data
import json



def main(path = "./sample_input/events.txt"):
    eventList = Data().__dict__
    eventList['customer'] = dict()
    eventList['siteVisit'] = dict()
    eventList['image'] = dict()
    eventList['order'] = dict()

    data = loadData(path)
    for e in data:
        ingest(e, eventList)
    print(eventList)
    return eventList
    TopXSimpleLTVCustomers(x, D)




def ingest(e, D):
    """
    Given event e, update data D
    :param e: an event
    :param D: new data
    :return: no need to return, will update values in place
    """
    if e['type'] == 'CUSTOMER':
        # if key is not exist, add new, else if not exist and verb equals to update, update object
        if e['key'] not in D['customer'].keys():
            D['customer'][e['key']] = Customer( e['type'], e['verb'], e['key'], e['event_time'], e['last_name'],
                                                e['adr_city'], e['adr_state'] )
        elif e['key'] in D['customer'].keys() and e['verb'] == 'UPDATE':
            updateCustomer( e, D )
    elif e['type'] == 'IMAGE':
        # if key is not exist, add new, else update object
        if e['key'] not in D['image'].keys():
            D['image'][e['key']] = Image( e['type'], e['verb'], e['key'], e['event_time'], e['customer_id'],
                                      e['camera_make'], e['camera_model'] )
        elif e['key'] in D['image'].keys():
            updateImage( e, D )
    elif e['type'] == 'ORDER':
        # if key is not exist, add new, else if not exist and verb equals to update, update object
        if e['key'] not in D['order'].keys():
            D['order'][e['key']] = Order( e['type'], e['verb'], e['key'], e['event_time'], e['customer_id'],
                                      e['total_amount'] )
        elif e['key'] in D['order'].keys() and e['verb'] == 'UPDATE':
            updateOrder( e, D )
    elif e['type'] == 'SITE_VISIT':
        # if key is not exist, add new, else update object
        if e['key'] not in D['siteVisit'].keys():
            D['siteVisit'][e['key']] = SiteVisit( e['type'], e['verb'], e['key'], e['event_time'], e['customer_id'],
                                              e['tags'] )
        elif e['key'] in D['siteVisit'].keys():
            updateSiteVisit( e, D )


def updateCustomer(e, D):
    """
    check if event has new value, update customer Data 
    :param e: an event
    :param D: new data
    :return: no need to return, will update values in place
    """
    for key, value in e.items():
        if value != None:
            D['customer'][e['key']].__dict__[key] = value

def updateOrder(e, D):
    """
    check if event has new value, update order Data 
    :param e: an event
    :param D: new data
    :return: no need to return, will update values in place
    """
    for key, value in e.items():
        if value != None:
            D['order'][e['key']].__dict__[key] = value

def updateImage(e, D):
    """
    check if event has new value, update image Data 
    :param e: an event
    :param D: new data
    :return: no need to return, will update values in place
    """
    for key, value in e.items():
        if value != None:
            D['customer'][e['key']].__dict__[key] = value

def updateSiteVisit(e, D):
    """
    check if event has new value, update visit Data 
    :param e: an event
    :param D: new data
    :return: no need to return, will update values in place
    """
    for key, value in e.items():
        if value != None:
            D['customer'][e['key']].__dict__[key] = value

def TopXSimpleLTVCustomers(x, D):
    """
    Return the top x customers with the highest Simple Lifetime Value from data D.
    :param x: an integer
    :param D: data
    :return: a list
    """
    res = dict()
    for cusId in D['customer'].keys():
        res[cusId] = calculateLTV(D)
    return sorted(res.values())[:x]
    with open('./output/output.txt','w') as output:
        for w in res:
            output.write(w)




def calculateLTV(D, t = 10):
    """
    simple LTV: 52(a) x t
    `a` is the average customer value per week, roughly a = s * c
        => ($/vist * visit/week) per customer
        => $/week per customer
    `s` is customer expenditures per visit (USD)
    `c` is number of site visits per week)
    `t` is the average customer lifespan. The average lifespan for Shutterfly is 10 years.  
        => t = 10
    :return: a float number of LTV
    """
    expense = sum( getOrderAmount( v ) for v in D['order'].values() )
    young = convertToWeek( max( v.__dict__['event_time'] for v in D['siteVisit'].values() ) )
    old = convertToWeek( min( v.__dict__['event_time'] for v in D['siteVisit'].values() ) )
    weeks = (young[0] - old[0]) * 52 + (young[1] - old[1])
    a = expense / weeks
    ltv = 52 * a * t
    return ltv

def revenuePerVisit(expense, visits):
    """
    helper function for calculating `s` in ltv
    s = expense / visits
    :return: float s, round to 2 decimal
    """
    return float("{0:.2f}".format(expense/visits))

def visitPerweek(visit, wknum):
    """
    helper function for calculating `c` in ltv
    c = visits / week
    :return: float c round to 2 decimal
    """
    return float("{0:.2f}".format(visit/wknum))


def getOrderAmount(order):
    """
    Extract numeric value from order's total amount which is in String format('12.34 USD').
    If there is not numeric value return 0.
    :param order: one order event
    :return: order total amount as a float number
    
    """
    nums = list(filter( lambda x: x.isnumeric(), order.total_amount))
    return (int(''.join(nums)) / 100) if len(nums) > 0 else 0

def convertToWeek(timestamp):
    """
    ASSUMING timestamp is either fully match %Y-%m-%dT%H:%M:%S.%fZ or none
    isocalendar() function in datetime will return a tuple, e.g. (year, week number, weekday)
    week number has a range from 1 to 52
    weekday has a range from 1 to 7, representing from Mon to Sun
    :param timestamp: datetime object
    :return: week number
    
    >>> convertToWeek('2017-01-06T12:46:46.384Z')
    (2017, 1, 5)
    """
    if not timestamp:
        print( 'timestamp is not valid' )
        return None
    time = parseTime(timestamp)
    return time.isocalendar()


def parseTime(timestamp):
    """
    ASSUMING timestamp is either fully match %Y-%m-%dT%H:%M:%S.%fZ or none
    In order to get week number and weekday number, use datetime library to parse timestamp.
    :param timestamp: event.event_time
    :return: datetime object
    """
    if not timestamp:
        print( 'timestamp is not valid' )
        return None
    from datetime import datetime
    return datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')


def loadData(path="../../sample_input/events.txt"):
    """
    ASSUMING the input data will be in text file with json format
    load date from text file, and save data in a list
    for test purpose, use sample input
    address = "./input/*.txt"
    :param path: file path
    :return: a list of event data in json format
    >>> len(loadData("./sample_input/events.txt"))
    4
    """
    # import json
    file = open( path, 'r' )
    data = file.read()
    content = json.loads( data )
    return content
