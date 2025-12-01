import http.client
try:
    conn = http.client.HTTPConnection("jsonplaceholder.typicode.com")
    conn.request("GET", "/")
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    print(data)
except http.client.HTTPException as e:
    print("HTTP error occurred:", e)
except Exception as e:
    print("An error occurred:", e)
finally:
    conn.close()