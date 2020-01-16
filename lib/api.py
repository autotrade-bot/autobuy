import pybitflyer
import os
def initialize():
    api = pybitflyer.API(api_key=os.environ["API_KEY"], api_secret=os.environ["API_SECRET"])
    return api
