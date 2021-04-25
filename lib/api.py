import pybitflyer
import os
def initialize():
    api = pybitflyer.API(api_key=os.environ["BITFLYER_API_KEY"], api_secret=os.environ["BITFLYER_API_SECRET"])
    return api
