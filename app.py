from flask import Flask, request, session, render_template
from currency import ConversionError, get_rates, validate_currency, currency_symbols

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"


@app.route("/", methods=['GET', 'POST'])
def show_home():
    converted_amount = None #Initialize as None by default
    converted_currency = None
    error_message = None

    if request.method == 'POST':
        try:
            amount = float(request.form.get('amount'))
            base_currency = request.form.get('from')
            target_currency = request.form.get('to')

            validate_currency(base_currency)
            validate_currency(target_currency)

            data = get_rates()
            exchange_rate = data['rates'][target_currency] / data['rates'][base_currency]
            converted_amount = amount * exchange_rate

            converted_amount = round(converted_amount, 2)

            converted_currency = currency_symbols.get(target_currency, target_currency)
        except ConversionError as e:
            error_message = str(e)
        except Exception as e:
            error_message = "An error has occured during conversion"

    return render_template('home.html', converted_amount=converted_amount, converted_currency=converted_currency, error_message=error_message)
    
 