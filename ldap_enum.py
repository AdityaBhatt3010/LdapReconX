import ldap3

# ===== USER INPUT =====
ip = input("Enter LDAP Server IP: ").strip()
dc1 = input("Enter Domain Component 1 (e.g., example): ").strip()
dc2 = input("Enter Domain Component 2 (e.g., local): ").strip()

user = input("Enter Username (leave blank for anonymous): ").strip()
password = input("Enter Password (leave blank for anonymous): ").strip()

# Construct search base
search_base = f"DC={dc1},DC={dc2}"

# ===== SERVER SETUP =====
server = ldap3.Server(ip, port=389, get_info=ldap3.ALL)

# ===== CONNECTION =====
if user and password:
    print("\n[+] Using Authenticated Bind...\n")
    conn = ldap3.Connection(
        server,
        user=f"{user}@{dc1}.{dc2}",
        password=password,
        authentication=ldap3.SIMPLE
    )
else:
    print("\n[+] Using Anonymous Bind...\n")
    conn = ldap3.Connection(server)

# ===== BIND =====
if conn.bind():
    print("[+] Bind Successful\n")

    print("[+] Server Info:\n")
    print(server.info, "\n")

    conn.search(
        search_base=search_base,
        search_filter='(objectClass=*)',
        attributes='*'
    )

    print("[+] LDAP Entries:\n")
    for entry in conn.entries:
        print(entry)

else:
    print("[-] Bind Failed")
