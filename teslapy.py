#!/usr/bin/env python

import os
import requests

email = os.environ.get('EMAIL')
teslaToken = os.environ.get('TESLATOKEN')
teslaVID = os.environ.get('TESLAVID')
teslaHeader = {'Authorization': teslaToken}
teslaAPI = "https://owner-api.teslamotors.com/api/1/vehicles/{teslaVID}/".format(teslaVID = teslaVID)

def vehicleData():
  r = requests.get("{teslaAPI}/vehicle_data".format(teslaAPI=teslaAPI), headers=teslaHeader)
  print(r.text)

