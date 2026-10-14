import requests
key = "c76c8f45962cefa65b0cf9b37eb5bc6a540325b190117fd6d7f007d86291eb1e"
headers = {"x-apikey":key}
# User se ip ly gy
ip = input("IP address dalo:")
url = f"https://virustotal.com/api/v3/ip_addresses/{ip}"
try:
    r = requests.get(url,headers=headers)
    data = r.json()
    # Agar ip ghalat ho
    if "error" in data:
        print(f"Error: {data['error']['message']}")
    else:
        stats = data['data']['attributes']['last_analysis_stats']
        malicious = stats['malicious']
        harmless = stats['harmless']
        owner = data['data']['attributes'].get('as_owner','unknown')
        print("\n---REPORT---")
        print(f"IP: {ip}")
        print(f"Owner: {owner}")
        print(f"Malicious: {malicious} | Harmless: {harmless}")
        # FINAL TEST
        if malicious==0:
           print("Result: Safe hai")
        elif malicious>=1 and malicious<5:
            print(f"Result: Suspicious hai {malicious} engines ne pakra")
        else:
            print(f"Result: Malicious hai Block kro {malicious} engines ne pakra ")
except Exception as e:
    print(f"Masla ho gya {e}")
        

