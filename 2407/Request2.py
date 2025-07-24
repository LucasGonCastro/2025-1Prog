import sys,requests

try:
    reqHTTP = requests.get("http://viacep.com.br/ws/59158-902/json")
except Exception as e:
    sys.exit(f"Erro:{e}")
else:
    if reqHTTP.status_code != 200:
        sys.exit("Erro na Requisisão ")
dictCEP = reqHTTP.json()
print(dictCEP) 
