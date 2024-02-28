import requests

link = "http://127.0.0.1:5000"

requisicao = requests.get(link)

print(requisicao)
print(requisicao.json())