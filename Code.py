import requests

def get_crypto_price(crypto='bitcoin', currency='usd'):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}'
    response = requests.get(url)
    data = response.json()
    
    if crypto in data:
        price = data[crypto][currency]
        return price
    else:
        print(f"Error: {crypto} not found.")
        return None

if name == "main":
    crypto = input("Enter cryptocurrency name (e.g. bitcoin): ").lower()
    currency = input("Enter currency (e.g. usd): ").lower()
    
    price = get_crypto_price(crypto, currency)
    
    if price:
        print(f"The current price of {crypto} in {currency} is: {price}")
