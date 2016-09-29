import twitter


class twitterAPI:

    def __init__(self):

        '''Create and return connection to thirstyGarden'''

        self.api = twitter.Api(consumer_key='',
                               consumer_secret='',
                               access_token_key='',
                               access_token_secret='')

    def junkNotification(self):
        self.api.PostUpdate("Just deleted a junk command", )

    def waterNotification(self, minutes):
        self.api.PostUpdate("Watered the garden for %d minutes." % minutes, )
