import requests
import datetime
import os


folder = '/tmp'


def pull_historic_rates(table='A', code='EUR', start_date='2013-01-01', end_date='2013-12-31'):
	URL = f"http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{start_date}/{end_date}?format=xml"
	response = requests.get(URL)
	start_date, end_date = start_date.replace('-', ''), end_date.replace('-', '')
	full_path = os.path.join(folder, f'{code}_{table}_{start_date}{end_date}.xml')
	with open(full_path, 'wb') as file:
		file.write(response.content)
		file.close()

	

def pull_todays_rate(table='A', code='EUR'):
	URL = f"http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/today?format=xml"
	response = requests.get(URL)
	full_path = os.path.join(folder, f'{code}_{table}_{datetime.date.today().strftime("%Y%m%d")}.xml') 
	with open(full_path, 'wb') as file:
		file.write(response.content)
		file.close()



for year in range(2013, 2021):
	start_date, end_date = f'{year}-01-01', f'{year}-12-31'
	pull_historic_rates(start_date=start_date, end_date=end_date)

today_string = datetime.date.today().strftime("%Y-%m-%d")
pull_historic_rates(start_date='2021-01-01', end_date=today_string)