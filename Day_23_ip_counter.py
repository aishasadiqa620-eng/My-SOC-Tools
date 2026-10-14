import re
failed_count=0
ip_count={}
with open("log.txt","r") as f:
    for line in f:
        if "failed" in line.lower():
            failed_count=failed_count+1
            ips=re.findall(r"\d+\.\d+\.\d+\.\d+",line)
            if ips:
                ip=ips[0]
                if ip in ip_count:
                    ip_count[ip]=ip_count[ip]+1
                else:
                    ip_count[ip]=1
print(f"Total failed:{failed_count}")
for ip,count in ip_count.items():
    print(f"{ip} : {count} times")

#-------Day 24 ka naya code yaha sy shuru-------
if ip_count:
    top_ip = max(ip_count,key=ip_count.get)
    top_count = ip_count[top_ip]
    print(f"[!] Top Attacker Found: {top_ip} -> {top_count} attacks")
else:
    print("Koi attack nhi mila")
    

            