import twitter


class TwitterAPI:

    def __init__(self):

        '''Create and return connection to thirstyGarden'''

        self.api = twitter.Api(consumer_key='',
                               consumer_secret='',
                               access_token_key='',
                               access_token_secret='')

    def junk_notification(self):
        self.api.PostUpdate("Just deleted a junk command", )

    def water_notification(self, minutes):
        self.api.PostUpdate("Watered the garden for %d minutes." % minutes, )
