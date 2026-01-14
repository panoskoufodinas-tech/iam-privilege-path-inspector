# Copyright 2026 panoskoufodinas-tech
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.import subprocess, json, os
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
