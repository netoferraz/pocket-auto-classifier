from configparser import ConfigParser
from pocket import Pocket
from misc.tags import tags
from misc.models import PocketData
from misc.funcs import retrieve_articles_from_tags
import pandas as pd
config = ConfigParser()
config.read('config.ini')
#credentials to access pocket api
POCKETCREDENTIALS = config['pocket']
CONSUMERKEY = POCKETCREDENTIALS['CONSUMERKEY']
ACCESSTOKEN = POCKETCREDENTIALS['ACCESSTOKEN']

#initialize pocket api
p = Pocket(consumer_key=CONSUMERKEY, access_token=ACCESSTOKEN)
#get data
data = retrieve_articles_from_tags(api=p, tags=tags)
#save data into csv file
pd.DataFrame(data).to_csv("./data/list_of_pocket_items.csv", sep=';', index=False)








