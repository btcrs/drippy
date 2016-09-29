from logging.config import fileConfig
import SprinklerGPIO
import TwitterLogin
import logging
import time
import re

fileConfig('../log.cfg')
logger = logging.getLogger("../logs/water_logged.txt")

thirstyGarden = TwitterLogin.thirstyGarden()
api = thirstyGarden.api


def waterWatcher():
    try:
        dripController = SprinklerGPIO.SprinklerGPIO(1)
        tweetsOnTimeline = api.GetUserTimeline('X')
        for x in range(len(tweetsOnTimeline)):
            tweets = [s.text for s in tweetsOnTimeline]
            water_instructions = re.compile(
                r"#waterMe \d+|#waterMe").search(tweets[0])
            if water_instructions is not None:
                found_options = water_instructions.group().split(" ")
            else:
                found_options = "No instructions found"

            if found_options[0] == '#waterMe':
                minutes = dripController.waterForXMinutes(0, found_options)
                logger.debug("The garden was watered for %d minutes" % minutes)
                thirstyGarden.waterNotification(minutes)
                api.DestroyStatus(tweetsOnTimeline[0].id)

            else:
                thirstyGarden.junkNotification()
                api.DestroyStatus(tweetsOnTimeline[0].id)

        print 'no tweets'
        # Avoid twitter rate limiting
        time.sleep(15)

    finally:
        if dripController.getStationStatus(0) == 1:
            dripController.setStationStatus(0, 0)

if __name__ == "__main__":
    while 1:
        waterWatcher()
