# Weather Web Servier created for job interview sample code 
# 8/2/23
from flask import *
import json, html
import restEndpointHelper
# You can combime the iports above but I like to separate standard classes from user created classes

app = Flask(__name__)


#Only Return the current weather
@app.route('/weather/now', methods=['GET', 'POST'])
def currentWeatherPage():
    try:
        # Avoid malicious input
        location = html.escape(str(request.args.get('city')))
        weatherData = restEndpointHelper.getTodaysForecast(location)
        jsonData = json.dumps(weatherData)
        return jsonData

    except ValueError as e:
        return 'Please provide a city', 501
    except NameError as e:
        return 'Go see the World Fair', 502
    except:
        return ''


# 7 Day Forecast
@app.route('/weather/sevenDay', methods=['GET', 'POST'])
def sevenDayWeatherPage():
    try:
        locationQuery = html.escape(str(request.args.get('city')))
        weatherData = restEndpointHelper.getSevenDayForecast(locationQuery)
        jsonData = json.dumps(weatherData)
        return jsonData
    except ValueError as e:
        return 'Please provide a city', 501
    except NameError as e:
        return 'Go see the World Fair', 502
    except:
        return ''


if __name__ == '__main__':
    app.run(port=5000)