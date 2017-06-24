# Shutterfly code challenge

from Shuxian Wu

## How to Run:

under code-challenge-Shuxian_Wu directory, run main.py with path to input file. Default path is set to sample_input directory.
In terminal, type `python -i src/ingestEvent/main.py` to access python console and call the functions.

## Assumptions:

1. Assuming data will be given either None value or correct in both value and formats. For future development, corner cases need to check.
2. All data in Data Dictionary will store as String. Additional parsing function will created for calculating LTV.
3. Assuming a in LTV can be calculated roughly equals to expense / weeks, but I also create function to calculate s and c.

## Tools

1. Programming language: Python 3.6
2. For easy ingestion and parsing, I used json and datetime libraries in python 3.6
3. Used PyCharm and Anaconda IDE for Python 3.6

## Analysis:

### Ingest:

There are 4 types of events, in order to keep this structure, I created entities package to store the hierarchy.
1. Create a parent object class called Event, then create 4 types of event object inheriting from Event class.

2. Create a data object to store ingested data in multilayer dictionary structure.

#### Ingested Data Output from sample input data:

{'customer': {'96f55c7d8f42': <src.entities.Customer.Customer object at 0x10d5aea58>},
'siteVisit': {'ac05e815502f': <src.entities.SiteVisit.SiteVisit object at 0x10d5ae9e8>},
'image': {'d8ede43b1d9f': <src.entities.Image.Image object at 0x10d5ae9b0>},
'order': {'68d84e5d1a43': <src.entities.Order.Order object at 0x10d5e1f60>}}

<key, value> pair for each layer in data dictionary :
    1. outer layer uses <type: dict{events}>
    2. middle layer uses <key: event object>
    3. inner layer uses <attributes: values>

### LTV:

According to the given instruction:

Simple LTV = 52(a) * t where t = 10

a = $/visits (s) * visits/weeks (c)

a: average customer value per week
c: number of site visits per week
s: customer expenditures per visit (USD)
t: average customer lifespan

Initially used dictionary to store output, but for better performance, I think a heap data structure will be a good option.

