# Mera pehla SOC Tool - Din 22
failed_count=0
with open("log.txt","r") as f:
    for line in f:
        if "failed" in line.lower():
            failed_count = failed_count+1
print(f"Total Failed login:{failed_count}")
if failed_count >2:
    print("Alert! BruteForce attack ho rha hy!")