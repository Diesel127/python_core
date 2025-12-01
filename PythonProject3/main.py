import http.client
import json
payload = json.dumps({
    "username": "Denis",
    "password": "Bykov"
})
headers = {
    'Content-Type': 'application/json'
}
try:
    conn = http.client.HTTPConnection("jsonplaceholder.typicode.com")
    conn.request("POST", "/posts", body=payload, headers=headers)
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    print(data)
except http.client.HTTPException as e:
    print("HTTP error occurred:", e)
except Exception as e:
    print("An error occurred:", e)
finally:
    conn.close()