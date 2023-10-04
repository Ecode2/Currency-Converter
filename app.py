from flask import Flask, render_template, request
from CurrencyConverter import currencyconvert

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def currency_converter():
    # Get post request from template
    if request.method == 'POST':

        # Get form info from html document
        from_currency = request.form['from_currency'].upper()
        to_currency = request.form['to_currency'].upper()
        amount = request.form['amount']

        # Defines the conversion login object
        conversion_logic = currencyconvert()

        # Gets the conversion information 
        result = conversion_logic.convert(from_currency, to_currency, amount)

        # Renders it on the html template
        return render_template('currencyconverter.html', result=result)

    return render_template('currencyconverter.html')

if __name__ == '__main__':
    app.run(debug=True)
