import http.client

conn = http.client.HTTPConnection("127.0.0.1:8000")

payload = "{\"nombre\":\"Restaurante 1\",\"direccion\":\"Calle 123, 123\",\"tipo_cocina\":\"Italiana\"}"

headers = { 'Authorization': "csrfmiddlewaretoken=nci9wmd6S22dsYVOpIvMZ8oDPbMNhpkx" }

conn.request("POST", "/restaurantes/create/", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))