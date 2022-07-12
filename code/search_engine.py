from datetime import date
from urllib import response
import requests
import json

# Collector get from thingiverse
# https://www.thingiverse.com/
# thing_id = thing:5412473
# author
# date
# title img
# create request to site, reciev


def GetFromThingiverse(terms:str):
        params={
                "access_token":"a3bff45acd0b641a2b318bbc82a3f990"
        }
        items=requests.get('https://api.thingiverse.com/search/{}'.format(terms),params=params).json()['hits']
        return items