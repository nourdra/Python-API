# Weather Web Servier Helper created for job interview sample code 
# 8/2/23
import time, random



#Return today's weather
def getTodaysForecast(city):

    checkInput(city)
    weatherData = {'Type': 'Now', 'Location' : city, 'Temp': tempByDay(city, 0), 'Time': time.time()}
    return weatherData


#Return Dict of 7 day forecast
def getSevenDayForecast(city):

    days = {}
    temps = {}

    checkInput(city)

    for i in range(7):
        temps = {'Temp': tempByDay(city, i)}
        days[i] = temps
            
        weatherData = {'Type':'7 Day Forcast', 
            'Location':city,
            'Day':days,
            'Time':time.time()}

    return weatherData

# Return daily temperatures
# This could be split up into different methods for the two options depending on the fecth cost and data set size.
# I could return the entire list for the seven day or the daily and grab what I need
# Or I could just grab for one day.  This simulates grabbing for one day
def tempByDay(location, offset):

    #This is a mock list of temperatures.  Normally this is where you get the data from a source but I'll just return a random temp
    #temps = ['94', '89', '87', '91', '95', '80', '88']
    #return temps[offs et]
    return random.randrange(80,100)

# Data integrety checks
def checkInput(city):

    if not city:
        raise ValueError('No Location Provided')
    elif city.upper() == 'KNOXVILLE':
        raise NameError('Why check when the weather its always beautiful in Knoxville')
