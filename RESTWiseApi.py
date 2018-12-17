# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import requests
from bs4 import BeautifulSoup
from easygui import *
from json import *


# ------------------------------------------------------------------------
#                       REST CODES
#  -----------------------------------------------------------------------

def restGetSummary(direccion, api_key):
    headers = {'Accept':'application/json', 'api_key': api_key}
    print headers
    data = requests.get(direccion, headers=headers)
    parsed = loads(data.content)
    codebox("","GetSummary Response", dumps(parsed, indent=4, sort_keys=True))
    return

# ------------------------------------------------------------------------
def restGetLastData(direccion, api_key, identificador):
    headers = {'Accept':'application/json', 'api_key': api_key}
    print headers
    direccion = direccion+identificador
    data = requests.get(direccion, headers=headers)
    print (data.url)
    parsed = loads(data.content)
    codebox("", "GetLastData Response", dumps(parsed, indent=4, sort_keys=True))
    return

# ------------------------------------------------------------------------
def restGetData(direccion, api_key,IDs, IDOperacion, IDInterval, initTime,endTime):
    headers = {'Accept':'application/json', 'api_key': api_key}
    print headers
    payload = {'ids':IDs,'idOperation':IDOperacion, 'idInterval':IDInterval, 'initTime':initTime, 'endTime': endTime}
    print "Payload:", payload
    print "Direccion:", direccion

    data = requests.get(direccion, headers=headers)
    print (data.url)
    print (data.content)
    parsed = loads(data.content)
    codebox("","GetData Response", dumps(parsed, indent=4, sort_keys=True))
    return

# ------------------------------------------------------------------------
def restGetDailyIrrigationData(direccion, api_key,identificador,initTime,endTime):
    headers = {'Accept':'application/json', 'api_key': api_key}
    print headers
    payload = {'ids':identificador, 'initTime':initTime, 'endTime': endTime}
    print payload
    data = requests.get(direccion, headers=headers)
    print (data.url)
    parsed = loads(data.content)
    codebox("","Get Daily Irrigation Data", dumps(parsed, indent=4, sort_keys=True))
    return

# ------------------------------------------------------------------------
def restSaveSubscription(direccion, api_key, queryParameters, period, expirationTime, channelParams):
    headers = {'Accept':'application/json', 'api_key': api_key}
    print headers
    payload = {'queryParameters':queryParameters, 'period':period, 'expirationTime': expirationTime,'channelParams': channelParams}
    print payload
    data = requests.get(direccion, headers=headers)
    print (data.url)
    parsed = loads(data.content)
    codebox("","Get Daily Irrigation Data", dumps(parsed, indent=4, sort_keys=True))
    return


# ------------------------------------------------------------------------
def restDeleteSubscription(direccion, api_key, id):
    headers = {'Accept':'application/json', 'api_key': api_key}
    print headers
    payload = {'subscriptionId':id}
    print payload
    data = requests.get(direccion, headers=headers)
    print (data.url)
    parsed = loads(data.content)
    codebox("Delete Subscription", dumps(parsed, indent=4, sort_keys=True))
    return


# ------------------------------------------------------------------------
def restGetFarms(direccion, api_key):
    headers = {'accept': 'application/json', 'api_key':api_key}
    print headers
    data = requests.get(direccion, headers=headers)
    print (data.url)
    parsed = loads(data.content)
    codebox("","getFarms Response", dumps(parsed, indent=4, sort_keys=True))
    return


# ------------------------------------------------------------------------
def restScheduledIrrigations(direccion, api_key, initTime, endTime, sectorIds, Operacion):
    headers = {'Accept': 'application/json', 'api_key': api_key}
    print headers
    payload = {'initTime': initTime , 'endTime': endTime, 'sectorIds': sectorIds}
    print "Payload:", payload

    if (Operacion == "READ"):
        data = requests.get(direccion, headers=headers)

    if (Operacion == "CREATE"):
        data = requests.post(direccion, headers=headers)


    if (Operacion == "UPDATE"):
        data = requests.put(direccion, headers=headers)


    if (Operacion == "DELETE"):
        data = requests.delete(direccion, headers=headers)

    print (data.url)
    parsed = loads(data.content)
    codebox("Programmed Irrigations", "get ScheduledIrrigations Response", dumps(parsed, indent=4, sort_keys=True))
    return



