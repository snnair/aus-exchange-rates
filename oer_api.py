import urllib.request, json
import datetime

##STATIC MODEL FOR THE OER API##
class OpenExchangeRates:
    APP_ID = 'e30cb9f804524d1cadda70fa74f33296'
    BASE_URL = "https://openexchangerates.org/api/"
    URL_LATEST = "https://openexchangerates.org/api/latest.json?app_id=" + APP_ID
    

def get_latest_exchange_rates():
    latest_exchange_rates_response = urllib.request.urlopen(OpenExchangeRates.URL_LATEST)
    latest_exchange_rates_data = latest_exchange_rates_response.read()
    latest_exchange_rates_data = json.loads(latest_exchange_rates_data)
    return latest_exchange_rates_data['rates']

def get_historical_exchange_rates(date):
    historical_url = OpenExchangeRates.BASE_URL+"historical/" + date +".json?app_id="+OpenExchangeRates.APP_ID
    historical_exchange_rates_response = urllib.request.urlopen(historical_url)
    historical_exchange_rates_data = historical_exchange_rates_response.read()
    historical_exchange_rates_data = json.loads(historical_exchange_rates_data)
    return historical_exchange_rates_data['rates']

def is_valid_date(date):
    date_picked = datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%d/%m/%Y')
    today = datetime.datetime.today().strftime('%d/%m/%Y')

    if today <= date_picked:
        return False
    return True
