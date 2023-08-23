import requests
import json
import time

def getSystemID(listofsystems):
    url = "https://esi.evetech.net/latest/universe/ids/" + listofsystems
    listofsystemIDs = response = requests.post(url).json()

    return(listofsystemIDs)


def getRoute(current_system, jove_obs_system):
    try:
        url = "https://esi.evetech.net/latest/route/" + current_system + "/" + jove_obs_system
        response = requests.get(url)
    except:
        time.sleep(5)
        try:
            url = "https://esi.evetech.net/latest/route/" + current_system + "/" + jove_obs_system
            response = requests.get(url)
        except:
            print("failed for ", jove_obs_system)
            response = requests.get(url)
            
    return(response.json())

def getSov():
    try:
        url = "https://esi.evetech.net/latest/sovereignty/structures/?datasource=tranquility"
        response = requests.get(url)
    except:
        response = "fail"

    return(response)
