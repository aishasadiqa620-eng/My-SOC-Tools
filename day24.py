import requests
key = "c76c8f45962cefa65b0cf9b37eb5bc6a540325b190117fd6d7f007d86291eb1e"
url = "https://www.virustotal.com/api/v3/ip_addresses/8.8.8.8"
headers = {"x-apikey":key}
r = requests.get(url,headers=headers)
print(r.json()['data']['attributes']['last_analysis_stats'])