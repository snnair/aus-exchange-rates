from flask import Flask, render_template, request, jsonify
import datetime
from oer_api import *


def create_app():

    app = Flask(__name__)

    ##ROUTES
    @app.route('/', methods = ['GET','POST'])
    def home():
        latest_exchange_rates = get_latest_exchange_rates()
        return render_template('index.html', rates = latest_exchange_rates)

    @app.route('/historical', methods = ['GET', 'POST'])
    def historical():
        date = request.form.get('historical_date_picker')

        if is_valid_date(date):
            date = datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%Y-%m-%d")
            historical_exchange_rates = get_historical_exchange_rates(date)
            return render_template('historical.html', rates = historical_exchange_rates)
        else:
            return jsonify({"Error":"The submitted date is not valid for a historical lookup."})
    return app