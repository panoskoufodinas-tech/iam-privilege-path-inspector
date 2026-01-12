import subprocess, json, os
def run():
    print("="*40 + "\n IPPI v2.0\n" + "="*40)
    proj = subprocess.getoutput("gcloud config get-value project 2>/dev/null").split()[-1]
    if not proj or "unset" in proj: return print("Error: No Project")
    print(f"[*] Target Locked: {proj}")
    raw_iam = subprocess.getoutput(f"gcloud projects get-iam-policy {proj} --format=json 2>/dev/null")
    try:
        iam = json.loads(raw_iam)
    except:
        return print("[!] ERROR: Could not parse IAM. Check permissions.")
    leaks = []
    for b in iam.get("bindings", []):
        role = b.get("role", "")
        for m in b.get("members", []):
            if "deleted:" in m.lower():
                risk = "HIGH" if any(x in role.lower() for x in ["owner", "editor", "admin"]) else "MEDIUM"
                leaks.append({"m":m, "r":role, "risk":risk})
                print(f"[!!!] {risk} RISK: {m} -> {role}")
    if leaks:
        with open("discovery.json", "w") as f: json.dump(leaks, f)
        print(f"[+] Found {len(leaks)} leaks. Saved to discovery.json")
    else: print("[+] Clean.")
run()