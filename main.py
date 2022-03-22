import requests
#import os
import datetime
now = datetime.datetime.now()
file_location = "Covid-19_report.txt"

url = 'https://coronavirus-19-api.herokuapp.com/countries/guyana'

req = requests.get(url)
output = req.json()

country = output['country']
cases = output['cases']
todayCases = output['todayCases']
deaths = output['deaths']
todayDeaths = output['todayDeaths']
recovered = output['recovered']
active = output['active']
critical = output['critical']
totalTests = output['totalTests']

deaths_percentage = (deaths/cases) * 100
percentage = (cases/totalTests) * 100
wasted_tests = 100 - percentage

f = open(file_location, "a")
f.write('Covid-19 Stats for ' + str(country) + '\n')
f.write('Total tests so far: ' + str(totalTests) + '\n')
f.write('Total cases so far: ' + str(cases) + '\n')
f.write('Total deaths so far: ' + str(deaths) + '\n')
f.write('Percentage of infected persons from tests = ' + str(round(percentage, 2)) + '%\n')
f.write('Percentage of tests wasted = ' + str(round(wasted_tests, 2)) + '%\n')
f.write('kill rate in ' + str(country) + ' is currently at: ' + str(round(deaths_percentage, 0)) + '%\n')
f.write(str(now)[:16] + '\n\n')
f.close()