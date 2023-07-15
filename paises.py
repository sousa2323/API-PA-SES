import json

import requests

URL_ALL = "https://restcountries.com/v2/all"
URL_NAME = "https://restcountries.com/v2/name/brazil"

resposta = requests.get(URL_ALL)


paises = json.loads(resposta.text) # PARSING de JSON para PYTHON

print(len(paises))

for pais in paises:
    print(pais['currencies'])
