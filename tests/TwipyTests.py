import unittest
import re
import sys
sys.path.append('../twipy')
from twipy import SprinklerGPIO


class OptionsInputTests(unittest.TestCase):

    def testGoodInput(self):
        goodInput = "I am searching for #waterMe"
        waterOptions = re.compile(r"#waterMe \d+|#waterMe")
        result = waterOptions.search(goodInput)
        self.assertEqual(result.group(), '#waterMe')

    def testGoodInputWithTime(self):
        goodInputWithTime = "I am searching for #waterMe 2"
        waterOptions = re.compile(r"#waterMe \d+|#waterMe")
        result = waterOptions.search(goodInputWithTime)
        self.assertEqual(result.group(), '#waterMe 2')

    def testBadInput(self):
        badInput = "Nothing here"
        waterOptions = re.compile(r"#waterMe \d+|#waterMe")
        result = waterOptions.search(badInput)
        self.assertEqual(result, None)

    def testFaultyTime(self):
        faultyTime = "#waterMe -2"
        waterOptions = re.compile(r"#waterMe \d+|#waterMe")
        result = waterOptions.search(faultyTime)
        self.assertEqual(result.group(), '#waterMe')


class GPIOTests(unittest.TestCase):

    def testNumberOfStations(self):
        dripController = SprinklerGPIO.SprinklerGPIO(1)
        self.assertEqual(dripController.numberOfStations, 1)

    def testOpenDrip(self):
        dripController = SprinklerGPIO.SprinklerGPIO(1)
        self.assertEqual(dripController.getStationStatus(0), 0)
        dripController.setStationStatus(0, 1)
        self.assertEqual(dripController.getStationStatus(0), 1)
        dripController.setStationStatus(0, 0)

    def testCloseDrip(self):
        dripController = SprinklerGPIO.SprinklerGPIO(1)
        self.assertEqual(dripController.getStationStatus(0), 0)
        dripController.setStationStatus(0, 1)
        dripController.setStationStatus(0, 0)
        self.assertEqual(dripController.getStationStatus(0), 0)
