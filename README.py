# Exchange-rates.python

import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline
from datetime import timedelta, datetime
import requests
import json



def currencies():
    values = []

    end = datetime.now()
    start = end - timedelta(days=30)
    tmp = start
    while tmp < end:
        date = tmp.strftime("%Y-%m-%d")
        tmp = tmp + timedelta(days=1)
        rate = getValue(date)
        values.append(rate)

    return values
print("please wait we are getting your info ...... ")

def getValue(date=""):
    response_url = "http://data.fixer.io/api/{}?access_key=76e040f65065f16aa9c83ac387b27e4c".format(date)
    response = requests.get(response_url)
    value = json.loads(response.text)
    return value["rates"]


# Add data
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10', 'Day 11', 'Day 12', 'Day 13',
        'Day 14', 'Day 15', 'Day 16', 'Day 17', 'Day 18', 'Day 19', 'Day 20', 'Day 21', 'Day 22', 'Day 23', 'Day 24', 'Day 25',
        'Day 26', 'Day 27', 'Day 28', 'Day 29', 'Day 30']
days1 = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7", "Day 8", "Day 9", "Day 10", "Day 11", "Day 12", "Day 13",
        "Day 14", "Day 15", "Day 16", "Day 17", "Day 18", "Day 19", "Day 20", "Day 21", "Day 22", "Day 23", "Day 24", "Day 25",
        "Day 26", "Day 27", "Day 28", "Day 29", "Day 30"]
rates = currencies()
MYR = []
AED = []
BRL = []
QAR = []
SAR = []
for i in range(30):
    MYR.append(rates[i]["MYR"])
    AED.append(rates[i]["AED"])
    BRL.append(rates[i]["BRL"])
    QAR.append(rates[i]["QAR"])
    SAR.append(rates[i]["SAR"])


#Sorting currinces

def sort(array, ):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater) # Just use the + operator to join lists
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

######

#We used zip function in wich it sort days array based on the currency rates:
MYR_DAYS = [x for _,x in sorted(zip(MYR, days1))]
AED_DAYS = [x for _,x in sorted(zip(AED, days1))]
BRL_DAYS = [x for _,x in sorted(zip(BRL, days1))]
QAR_DAYS = [x for _,x in sorted(zip(QAR, days1))]
SAR_DAYS = [x for _,x in sorted(zip(SAR, days1))]

MYR_SORTED = sort(MYR) #sorting myr rates
AED_SORTED = sort(AED) #sorting aed rates
BRL_SORTED = sort(BRL) #sorting brl rates
QAR_SORTED = sort(QAR) #sorting qar rates
SAR_SORTED = sort(SAR) #sorting sar rates

######

# Create and style traces - before sorting:
trace0 = go.Scatter(
    x=days,
    y=MYR,
    name='MYR',
    line=dict(
        color='rgb(0, 0, 255)',
        width=4)
)
trace1 = go.Scatter(
    x=days,
    y=AED,
    name='AED',
    line=dict(
        color='rgb(204, 0, 102)',
        width=4, )
)
trace2 = go.Scatter(
    x=days,
    y=BRL,
    name='BRL',
    line=dict(
        color='rgb(51, 204, 51)',

        width=4,
    )  # dash options include 'dash', 'dot', and 'dashdot'
)
trace3 = go.Scatter(
    x=days,
    y=QAR,
    name='QAR',
    line=dict(
        color='rgb(51, 102, 153)',
        width=4,
    )
)
trace4 = go.Scatter(
    x=days,
    y=SAR,
    name='SAR',
    line=dict(
        color='rgb(255, 161, 0)',
        width=4,
    )
)

# data = [trace0]
data = [trace0, trace1, trace2, trace3, trace4]

# Edit the layout
layout = dict(title='Exchange Rates For Last 30 Days - Before Sorting',
              xaxis=dict(title='days'),
              yaxis=dict(title='Value',),
              )
# tickvals = [i * 0.01 for i in range(1, 500)]
fig = dict(data=data, layout=layout)
offline.plot(fig, filename='exchange.html')

#########

# Create and style traces - after sorting:
trace5 = go.Scatter(
    x=MYR_DAYS,
    y=MYR_SORTED,
    name='MYR',
    line=dict(
        color='rgb(0, 0, 255)',
        width=4)
)
trace6 = go.Scatter(
    x=AED_DAYS,
    y=AED_SORTED,
    name='AED',
    line=dict(
        color='rgb(204, 0, 102)',
        width=4, )
)
trace7 = go.Scatter(
    x=BRL_DAYS,
    y=BRL_SORTED,
    name='BRL',
    line=dict(
        color='rgb(51, 204, 51)',

        width=4,
    )  # dash options include 'dash', 'dot', and 'dashdot'
)
trace8 = go.Scatter(
    x=QAR_DAYS,
    y=QAR_SORTED,
    name='QAR',
    line=dict(
        color='rgb(51, 102, 153)',
        width=4,
    )
)
trace9 = go.Scatter(
    x=SAR_DAYS,
    y=SAR_SORTED,
    name='SAR',
    line=dict(
        color='rgb(255, 161, 0)',
        width=4,
    )
)

# data = [trace0]
data1 = [trace5]

# Edit the layout
layout1 = dict(title='MYR Exchange Rates For Last 30 Days - After Sorting',
              xaxis=dict(title='Days'),
              yaxis=dict(title='Value',),
              )
# tickvals = [i * 0.01 for i in range(1, 500)]
fig = dict(data=data1, layout=layout1)
offline.plot(fig, filename='exchangeMYR.html')

data2 = [trace6]

# Edit the layout
layout2 = dict(title='AED Exchange Rates For Last 30 Days - After Sorting',
              xaxis=dict(title='Days'),
              yaxis=dict(title='Value',),
              )
# tickvals = [i * 0.01 for i in range(1, 500)]
fig = dict(data=data2, layout=layout2)
offline.plot(fig, filename='exchangeAED.html')

data3 = [trace7]

# Edit the layout
layout3 = dict(title='BRL Exchange Rates For Last 30 Days - After Sorting',
              xaxis=dict(title='Days'),
              yaxis=dict(title='Value',),
              )
# tickvals = [i * 0.01 for i in range(1, 500)]
fig = dict(data=data3, layout=layout3)
offline.plot(fig, filename='exchangeBRL.html')

data4 = [trace8]

# Edit the layout
layout4 = dict(title='QAR Exchange Rates For Last 30 Days - After Sorting',
              xaxis=dict(title='Days'),
              yaxis=dict(title='Value',),
              )
# tickvals = [i * 0.01 for i in range(1, 500)]
fig = dict(data=data4, layout=layout4)
offline.plot(fig, filename='exchangeQAR.html')

data5 = [trace9]

# Edit the layout
layout5 = dict(title='SAR Exchange Rates For Last 30 Days - After Sorting',
              xaxis=dict(title='Days'),
              yaxis=dict(title='Value',),
              )
# tickvals = [i * 0.01 for i in range(1, 500)]
fig = dict(data=data5, layout=layout5)
offline.plot(fig, filename='exchangeSAR.html')
