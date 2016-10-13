from logging.config import fileConfig
import sprinkler_gpio
import logging
import time
import twitter_api
import re

fileConfig('../log.cfg')
logger = logging.getLogger("../logs/water_logged.txt")

# Needs filled out with personal information
thirsty_garden = twitter_api.Twitter_API()

def water_watcher():
    try:
        drip_controller = sprinkler_gpio.SprinklerGPIO(1)
        tweets_on_timeline = thirsty_garden.api.get_user_timeline('X')

        for tweet in tweets_on_timeline:
            water_instructions = re.compile( r"#waterMe \d+|#waterMe") \
                                   .search(tweet.text)                 \
                                   .group()                            \
                                   .split(" ")                         \

            if water_intstructions[0] == '#waterMe':
                minutes = drip_controller.waterForXMinutes(0, water_instructions)
                logger.debug("The garden was watered for %d minutes" % minutes)
                thirsty_garden.water_notification(minutes)
                thirsty_garden.api.DestroyStatus(tweet.id)

            else:
                thirsty_garden.junkNotification()
                thirsty_garden.api.DestroyStatus(tweet.id)


    finally:
        if drip_controller.getStationStatus(0) is 1:
            drip_controller.setStationStatus(0, 0)
        time.sleep(15)

def main():
    while True:
        print("sup")
        water_watcher()

if __name__ == "__main__":
    main()
