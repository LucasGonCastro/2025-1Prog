import sys,requests

try:
    reqHTTP = requests.get("https://api.cartola.globo.com/atletas/mercado")
except Exception as e:
    sys.exit(f"Erro:{e}")
else:
    if reqHTTP.status_code != 200:
        sys.exit("Erro na Requisisão ")
dictCartola = reqHTTP.json()
print(dictCartola)