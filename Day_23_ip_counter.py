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
    

            