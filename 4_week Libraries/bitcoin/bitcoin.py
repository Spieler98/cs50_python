import requests
import sys

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    json = r.json()
except requests.RequestException:
    pass
bitcoin = float(json["bpi"]["USD"]["rate_float"])

if len(sys.argv) == 2:
    if sys.argv[1]:
        try:
            sys.argv[1] = float(sys.argv[1])
            value = sys.argv[1] * bitcoin
            print(f"{value:,}")
        except ValueError:
            sys.exit()