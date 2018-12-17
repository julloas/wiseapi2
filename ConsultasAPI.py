# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import RESTWiseApi
from easygui import *

# Oficial SSL API
restURL ="https://apiv2.wiseconn.com/"



def main():
    msg = "Enter logon information"
    title = "WiseAPI Version 2 - Demo"
    logonNames = ["APIKey:"]
    logonValues = multpasswordbox(msg, title, logonNames)
    token = logonValues[0]

    while(1):
        msg = "What Method do you like to test?"
        title = "WiseAPI Demo Software"
        choices = ["Get Farms",  "Get Last Data"] #"Get Data", "Get Daily Irrigation Data","Scheduled Irrigations"]
        choice = choicebox(msg, title, choices)

        if (choice == "Get Last Data"):
            RESTWiseApi.restGetLastData(restURL+'measures/', token, enterbox("ID Sensor","ID"))

      #  if (choice == "Get Data"):
      #       msg = "Enter the Data information. \nOperation\nAVERAGE = 0 , MAX = 1 , MIN = 2 , SUM = 3 , COUNT = 4\n\nInterval\nHOUR = 0 , DAY = 1 , MONTH = 2"
      #       title = "Get Data Method"
      #       fieldNames = ["Sensor ID", "Operation", "Interval", "Init Time", "End Time"]
      #       fieldValues = multenterbox(msg, title, fieldNames)
      #       RESTWiseApi.restGetData(restURL+'/rest/read/data', token, fieldValues[0],fieldValues[1],fieldValues[2],fieldValues[3],fieldValues[4])

      #  if (choice == "Get Daily Irrigation Data"):
      #      msg = "Enter the information."
      #      title = "Get Daily Irrigation"
      #      fieldNames = ["Sector ID", "Init Time", "End Time"]
      #      fieldValues = multenterbox(msg, title, fieldNames)
      #      RESTWiseApi.restGetDailyIrrigationData(restURL+'/rest/read/dailyIrrigationData', token,fieldValues[0],fieldValues[1],fieldValues[2] )

        if (choice == "Get Farms"):
            RESTWiseApi.restGetFarms(restURL+'farms', token)

      #  if (choice == "Scheduled Irrigations"):
      #      msg = "Enter the information. \n Operations: \n CREATE , UPDATE , DELETE , READ \n Example Sector: 8478"
      #      title = "New Scheduled Irrigations"
      #      fieldNames = ["Init Time", "End Time","Sector ID", "Operation"]
      #      fieldValues = multenterbox(msg, title, fieldNames)
      #      RESTWiseApi.restScheduledIrrigations(restURL+'/rest/write/scheduledIrrigations', token,fieldValues[0],fieldValues[1],fieldValues[2],fieldValues[3] )

        msg = "Do you want to continue?"
        title = "Please Confirm"
        if ccbox(msg, title):     # show a Continue/Cancel dialog
            pass  # user chose Continue
        else:
            sys.exit(0)           # user chose Cancel

main()
