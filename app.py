from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
import requests, sys, json
from datetime import datetime, timedelta


app = Flask(__name__)

#constantes
base_url = 'http://apilayer.net/api/historical?access_key=baf8800f7ce3994c54b6d234998d3118&currencies=BRL,EUR,ARS&format=1&date='
brazilian_real = 'USDBRL'
european_euro = 'USDEUR'
argentine_peso = 'USDARS'
n_days_ago = 7

def get_currencies(url):
	query = url
	try:
	    response = requests.get(query)
	    if response.status_code != 200:
			response = 'N/A'
	    else:
			rates = response.json()
			rate_in_currencies =(rates['quotes'])
			return rate_in_currencies
	except requests.ConnectionError as error:
	    print(error)
	    sys.exit(1)


def rate_in_currencies_week():
	dates = []
	for i in xrange(0,n_days_ago):
		date_n_days_ago = datetime.now().date() - timedelta(days=i)
		dates.append(date_n_days_ago)
	return dates #7 dates

def	convert_quote(real_quotes, any_quotes):
	converted_quote = real_quotes/any_quotes
	return converted_quote

@app.route('/') 
def index():
	converted_real = []
	converted_euro = []
	converted_peso = []
	week_array = (rate_in_currencies_week())
		
	#create an url with 1 day at loop
	for day in week_array:
		dictonary_of_currencies = get_currencies(base_url+str(day))
		real = (dictonary_of_currencies[brazilian_real])
		euro = (dictonary_of_currencies[european_euro])
		peso = (dictonary_of_currencies[argentine_peso])

		converted_real.append([day,real])
		converted_euro.append([day,convert_quote(real,euro)])
		converted_peso.append([day,convert_quote(real,peso)])

	return render_template('index.html', converted_real=converted_real, converted_euro=converted_euro, converted_peso=converted_peso)














