# Weather Web Servier Helper Test Class created for job interview sample code 
# 8/3/23
import unittest
import restEndpointHelper

class TestRestEndpoint(unittest.TestCase):
    
    #Test to see if we get 7 days of temperatures returned
    def test_sevenDay(self):
        testData = restEndpointHelper.getSevenDayForecast('Truth Or Consequences')
        self.assertEqual(len(testData["Day"]), 7)

    #Check to see the new ice age has not hit
    def test_today(self):
        testData = restEndpointHelper.getTodaysForecast('Kalamazoo')
        self.assertGreater(int(testData.get("Temp")), -100)

