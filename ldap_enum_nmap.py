import os

# ===== USER INPUT =====
ip = input("Enter Target IP: ").strip()
dc1 = input("Enter DC1 (e.g., example): ").strip()
dc2 = input("Enter DC2 (e.g., local): ").strip()

user = input("Enter Username (leave blank for anonymous): ").strip()
password = input("Enter Password (leave blank for anonymous): ").strip()

# ===== COMMAND LOGIC =====
if user and password:
    print("\n[+] Running Credentialed LDAP Search...\n")
    cmd = f'nmap -p 389 --script ldap-search --script-args "ldap.username={user}@{dc1}.{dc2},ldap.password={password},ldap.base=dc={dc1},dc={dc2}" {ip}'
else:
    print("\n[+] Running LDAP Brute (Anonymous Mode)...\n")
    cmd = f'nmap -p 389 --script ldap-brute --script-args "ldap.base=dc={dc1},dc={dc2}" {ip}'

# Execute
os.system(cmd)
