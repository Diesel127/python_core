import http.client

proxy_port = 3128
proxy_host = "10.10.1.0"
conn = http.client.HTTPConnection(proxy_host, proxy_port)
dest_url = 'httpbin.org'
dest_path = "/ip"
conn.set_tunnel(dest_url)
conn.request("GET", dest_path, headers={"Host": dest_url})
response = conn.getresponse()
print(response.read().decode('utf-8'))
conn.close()