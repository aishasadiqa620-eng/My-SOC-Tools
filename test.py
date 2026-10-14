import requests

try:
    r = requests.get("https://www.google.com",timeout=5)
    print(r.status_code)
except Exception as e:
    print("Error aya:",e)