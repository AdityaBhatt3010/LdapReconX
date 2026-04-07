#!/bin/bash

read -p "Enter Target IP: " ip
read -p "Enter DC1 (e.g., example): " dc1
read -p "Enter DC2 (e.g., local): " dc2

read -p "Enter Username (leave blank for anonymous): " user
read -p "Enter Password (leave blank for anonymous): " pass

if [[ -n "$user" && -n "$pass" ]]; then
    echo "[+] Running Credentialed LDAP Search..."
    nmap -p 389 --script ldap-search \
      --script-args "ldap.username=$user@$dc1.$dc2,ldap.password=$pass,ldap.base=dc=$dc1,dc=$dc2" \
      $ip
else
    echo "[+] Running LDAP Brute (Anonymous Mode)..."
    nmap -p 389 --script ldap-brute \
      --script-args "ldap.base=dc=$dc1,dc=$dc2" \
      $ip
fi
