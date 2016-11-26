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

def get_currencies():
	query = base_url
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
	# currency = (dictionary_of_currency[currency_country])
	for i in xrange(0,n_days_ago):
		date_n_days_ago = datetime.now().date() - timedelta(days=i)
		print(base_url+ str(date_n_days_ago))
	return str(date_n_days_ago)


@app.route('/') 
def index():
	dictonary_of_currencies = get_currencies()
	real = (dictonary_of_currencies[brazilian_real])
	euro = (dictonary_of_currencies[european_euro])
	peso = (dictonary_of_currencies[argentine_peso])
	rate_in_currencies_week()
	return render_template('index.html')