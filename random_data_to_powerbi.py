import random, requests, time
from datetime import datetime

# REST API endpoint, given to you when you create an API streaming dataset
# Will be of the format: https://api.powerbi.com/beta/<tenant id>/datasets/< dataset id>/rows?key=<key id>
REST_API_URL = "https://api.powerbi.com/beta/f4232552-7d9c-457b-8892-fd4de0de2d58/datasets/b9d220c8-5dcc-4df7-b42d-18b72ff6f7b1/rows?key=9I%2Fi%2FzcdqHMvAy7zQSSATaH3SKFWnrIAPsK4HU6hLcoFaxk5cAfPj1d8Pv9vAfedCG%2F6LNJO1xOUcdB%2Fw2j4yg%3D%3D"

while True:
    try:
        humidity = random.randint(1,101)
        temp = random.randint(1,35)
        print('Temp={0:0.1f} Humidity={1:0.1f}'.format(temp, humidity))

        now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S%Z")

        data = '[{{ "timestamp": "{0}", "temperature": "{1:0.1f}", "humidity": "{2:0.1f}" }}]'.format(now, temp, humidity)

        # make HTTP POST request to Power BI REST API
        r = requests.post(REST_API_URL, data=data)
        print(r.text)

        print("POST request to Power BI with data:{0}".format(data))

        time.sleep(1)

    except IOError:
        print('Error')