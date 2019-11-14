from configparser import ConfigParser
from pocket import Pocket
from misc.tags import tags
from misc.models import PocketData
from misc.funcs import retrieve_articles_from_tags
config = ConfigParser()
config.read('config.ini')
POCKETCREDENTIALS = config['pocket']

#credentials to access pocket api
CONSUMERKEY = POCKETCREDENTIALS['CONSUMERKEY']
ACCESSTOKEN = POCKETCREDENTIALS['ACCESSTOKEN']

#initialize pocket api
p = Pocket(consumer_key=CONSUMERKEY, access_token=ACCESSTOKEN)

data = retrieve_articles_from_tags(api=p, tags=tags)
            








