# LDAP Enumeration Toolkit

A modular toolkit for LDAP enumeration and Nmap-based credential testing in Active Directory environments.

![LdapRecoxX](https://github.com/user-attachments/assets/d181b503-1aa9-4f1e-991e-283a62e5ccc8) <br/>

---

## 🚀 Features

### 🔹 LDAP Enumeration (Python - ldap3)
- Anonymous bind testing
- Credential-based authentication
- Full directory enumeration
- Server metadata extraction

### 🔹 Nmap Integration
- LDAP brute-force testing (`ldap-brute`)
- Credentialed LDAP queries (`ldap-search`)
- Cross-platform support (.py, .sh, .bat)

---

## 📂 Project Structure

```

ldap-toolkit/
│
├── ldap_enum.py              # LDAP enumeration (ldap3 only)
├── ldap_enum_nmap.py         # Nmap via Python (os.system)
├── ldap_enum_nmap.sh         # Nmap (Linux/macOS)
├── ldap_enum_nmap.bat        # Nmap (Windows)
└── README.md

```

---

## 📦 Requirements

### 🔹 Python Dependencies
```

pip install ldap3

```

### 🔹 System Tools
- Nmap (installed & added to PATH)

---

## 🐍 Usage

### ▶️ LDAP Enumeration
```

python ldap_enum.py

```

#### Inputs:
- Target IP
- Domain Components (e.g., `example`, `local`)
- Username (optional)
- Password (optional)

---

### ▶️ Nmap (Python Wrapper)
```

python ldap_enum_nmap.py

```

---

### 🐧 Linux / macOS
```

chmod +x ldap_enum_nmap.sh
./ldap_enum_nmap.sh

```

---

### 🪟 Windows
```

ldap_enum_nmap.bat

```

---

## ⚙️ How It Works

### 🔓 Without Credentials
- Attempts anonymous LDAP bind
- Runs `ldap-brute` via Nmap

### 🔐 With Credentials
- Performs authenticated LDAP bind
- Runs `ldap-search` via Nmap

---

## 🔥 Example

### Domain:
```

example.local

```

### Search Base:
```

DC=example,DC=local

```

### User:
```

[john@example.local](mailto:john@example.local)

```

---

## 🧠 Use Cases

- Active Directory enumeration
- Misconfiguration detection (anonymous bind)
- Credential validation
- Internal pentesting labs
- Red Team recon workflows

---

## ⚠️ Disclaimer

This project is intended for **educational purposes and authorized security testing only**.  
Unauthorized use against systems you do not own or have permission to test is illegal.

---
