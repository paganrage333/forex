import requests

class ConversionError(Exception):
    pass

def get_rates():
    url = 'https://api.exchangerate.host/latest'
    response = requests.get(url)
    data = response.json()
    return data

def validate_currency(currency):
    valid_currencies = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNH', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'SSP', 'STD', 'STN', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPD', 'XPF', 'XPT', 'YER', 'ZAR', 'ZMW', 'ZWL']
    if currency not in valid_currencies:
        raise ConversionError(f"Invalid currency: {currency}")
    
currency_symbols = {
    'USD': '$',   # United States Dollar
    'EUR': '€',   # Euro
    'JPY': '¥',   # Japanese Yen
    'GBP': '£',   # British Pound Sterling
    'AUD': '$',   # Australian Dollar
    'CAD': '$',   # Canadian Dollar
    'CHF': 'CHF', # Swiss Franc
    'CNY': '¥',   # Chinese Yuan
    'SEK': 'kr',  # Swedish Krona
    'NZD': '$',   # New Zealand Dollar
    'MXN': '$',   # Mexican Peso
    'SGD': '$',   # Singapore Dollar
    'HKD': '$',   # Hong Kong Dollar
    'NOK': 'kr',  # Norwegian Krone
    'KRW': '₩',   # South Korean Won
    'TRY': '₺',   # Turkish Lira
    'RUB': '₽',   # Russian Ruble
    'INR': '₹',   # Indian Rupee
    'BRL': 'R$',  # Brazilian Real
    'ZAR': 'R',   # South African Rand
}
